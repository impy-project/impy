from pathlib import Path
from impy.constants import GeV
from impy.kinematics import EventKinematics
from impy.writer import HepMCWriter
import impy.models as im
import pytest
import pyhepmc
from .util import run_in_separate_process

basename = Path(__file__).with_suffix("")


def run(Model):
    ekin = EventKinematics(ecm=10 * GeV, p1pdg=2212, p2pdg=2212)
    gen = Model(ekin, seed=1)
    return list(ev.copy() for ev in gen(3))


@pytest.mark.parametrize(
    "Model",
    [
        im.Sibyll21,
        im.Pythia6,
        im.EposLHC,
    ],
)
def test_hepmc_writer(Model):
    # To run this test do `pytest tests/test_hepmc_writer.py`
    # This test fails because the event record written by HepMC3 C++ is bad,
    # a lot of particles are missing. Either a bug in the original impy record or a
    # bug in the HepMC3 C++ code (not the pyhepmc code).

    if Model is im.EposLHC:
        pytest.xfail("EposLHC has indices that are out of range")

    test_file = Path(f"{basename}_{Model.__name__}.dat")

    events = run_in_separate_process(run, Model)

    expected = []
    with HepMCWriter(str(test_file)) as w:
        for event in events:
            w.write(event)
            expected.append(event.to_hepmc3())

    restored = []
    for event in pyhepmc.open(str(test_file)):
        assert event is not None
        # Some models (e.g. Sibyll) do not set event.event_number properly
        # assert event.event_number == ievent
        restored.append(event)

    for ev1, ev2 in zip(expected, restored):
        assert ev1 == ev2

    # delete test_file if test is successful
    test_file.unlink()
