from chromo.kinematics import CenterOfMass
from chromo import models as im
from chromo.constants import GeV
from chromo.models.sophia import Sophia20
from .util import run_in_separate_process
from chromo.util import get_all_models
import numpy as np
import pytest

# generate list of all models in chromo.models
models = get_all_models()


def run(Model):
    evt_kin = CenterOfMass(10 * GeV, "proton", "proton")
    if Model is Sophia20:
        evt_kin = CenterOfMass(10 * GeV, "photon", "proton")
    m = Model(evt_kin, seed=1)
    for event in m(100):
        if len(event) > 10:  # to skip small events
            break
    return event  # MCEvent is pickeable, but restored as EventData


@pytest.mark.parametrize("Model", models)
def test_to_hepmc3(Model):
    if Model.name in ("PhoJet", "DPMJET-III"):
        # hepmc history is different from the history
        # contained in mothers and daughters
        # see `util.phojet_dpmjet_hepmc` function
        pytest.xfail(
            "PhoJet and DPMJET-III has complex history, "
            "so for now their hepmc history contains "
            "only final particles, should be FIXED!!!"
        )

    event = run_in_separate_process(run, Model)
    # special case for Pythia8, which does not contain the parton shower
    if Model is im.Pythia8:
        # parton shower is skipped
        from chromo.constants import quarks_and_diquarks_and_gluons

        ma = True
        apid = np.abs(event.pid)
        for p in quarks_and_diquarks_and_gluons:
            ma &= apid != p
        event = event[ma]

    unique_vertices = {}
    for i, pa in enumerate(event.mothers):
        assert pa.shape == (2,)
        if np.all(pa == -1):
            continue
        # normalize intervals
        if pa[1] == -1:
            pa = (pa[0], pa[0])
        pa = (pa[0], pa[1])
        # in case of overlapping ranges of incoming particles
        # the earlier vertex keeps them
        for a, b in unique_vertices:
            if pa != (a, b) and a <= pa[0] <= b:
                pa = b + 1, pa[1]
        unique_vertices.setdefault(pa, []).append(i)

    # check that parent ranges do not exceed particle range;
    # that's a requirement for a valid particle history
    nmax = len(event.px)
    for i, (a, b) in enumerate(unique_vertices):
        assert a >= -1
        assert b <= nmax - 1, (
            f"vertex {i} has parent range {(a, b)} which "
            f"exceeds particle record nmax={nmax - 1}"
        )

    # not all vertices have locations different from zero,
    # create unique fake vertex locations for testing
    for ch in unique_vertices.values():
        i = ch[0]
        event.vx[i] = i
        event.vy[i] = i + 1
        event.vz[i] = i + 2
        event.vt[i] = i + 3

    hev = event.to_hepmc3()

    assert len(hev.run_info.tools) == 1
    assert hev.run_info.tools[0] == (*event.generator, "")
    assert len(hev.particles) == len(event)
    assert len(hev.vertices) == len(unique_vertices)

    for i, p in enumerate(hev.particles):
        assert p.momentum.x == event.px[i]
        assert p.momentum.y == event.py[i]
        assert p.momentum.z == event.pz[i]
        assert p.momentum.e == event.en[i]
        assert p.status == event.status[i]
        assert p.pid == event.pid[i]
        assert p.id == i + 1

    for i, v in enumerate(hev.vertices):
        k = v.particles_out[0].id - 1
        assert v.position.x == event.vx[k]
        assert v.position.y == event.vy[k]
        assert v.position.z == event.vz[k]
        assert v.position.t == event.vt[k]

    hev_vertices = {}
    for v in hev.vertices:
        pi = [p.id - 1 for p in v.particles_in]
        if len(pi) == 1:
            pa = (pi[0], pi[0])
        else:
            pa = (min(pi), max(pi))
        children = [p.id - 1 for p in v.particles_out]
        hev_vertices[pa] = children

    assert unique_vertices == hev_vertices
