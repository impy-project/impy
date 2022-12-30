from impy.util import pdg2AZ, name2pdg
from particle import Particle, literals as lp


def test_name2pdg():
    for p in Particle.findall():
        if p.name in ("n", "n~", "p", "p~"):  # special cases, treated below
            continue
        assert name2pdg(p.name) == p.pdgid
        assert name2pdg(p.programmatic_name) == p.pdgid
    assert name2pdg("proton") == lp.proton.pdgid
    assert name2pdg("neutron") == lp.neutron.pdgid
    assert name2pdg("p") == lp.proton.pdgid
    assert name2pdg("n") == lp.neutron.pdgid
    assert name2pdg("antiproton") == -lp.proton.pdgid
    assert name2pdg("antineutron") == -lp.neutron.pdgid
    assert name2pdg("pbar") == -lp.proton.pdgid
    assert name2pdg("nbar") == -lp.neutron.pdgid
    assert name2pdg("p~") == -lp.proton.pdgid
    assert name2pdg("n~") == -lp.neutron.pdgid
    assert name2pdg("photon") == lp.gamma.pdgid
    assert name2pdg("gamma") == lp.gamma.pdgid
    assert name2pdg("g") == 21  # gluon, not photon


def test_nuclei():
    nucleus = {
        "n": (1, 0),
        "p": (1, 1),
        "D2": (2, 1),
        "T3": (3, 1),
        "H4": (4, 1),
        "He4": (4, 2),
        "He5": (5, 2),
        "He6": (6, 2),
        "He7": (7, 2),
        "He8": (8, 2),
        "He9": (9, 2),
        "He10": (10, 2),
        "Li4": (4, 3),
        "Li5": (5, 3),
        "Li6": (6, 3),
        "Li7": (7, 3),
        "Li8": (8, 3),
        "Li9": (9, 3),
        "Li10": (10, 3),
        "Li11": (11, 3),
        "Li12": (12, 3),
        "Be5": (5, 4),
        "Be6": (6, 4),
        "Be7": (7, 4),
        "Be8": (8, 4),
        "Be9": (9, 4),
        "Be10": (10, 4),
        "Be11": (11, 4),
        "Be12": (12, 4),
        "Be13": (13, 4),
        "Be14": (14, 4),
        "B7": (7, 5),
        "B8": (8, 5),
        "B9": (9, 5),
        "B10": (10, 5),
        "B11": (11, 5),
        "B12": (12, 5),
        "B13": (13, 5),
        "B14": (14, 5),
        "B15": (15, 5),
        "B16": (16, 5),
        "B17": (17, 5),
        "B18": (18, 5),
        "B19": (19, 5),
        "C8": (8, 6),
        "C9": (9, 6),
        "C10": (10, 6),
        "C11": (11, 6),
        "C12": (12, 6),
        "C13": (13, 6),
        "C14": (14, 6),
        "C15": (15, 6),
        "C16": (16, 6),
        "C17": (17, 6),
        "C18": (18, 6),
        "C19": (19, 6),
        "C20": (20, 6),
        "C21": (21, 6),
        "C22": (22, 6),
        "N10": (10, 7),
        "N11": (11, 7),
        "N12": (12, 7),
        "N13": (13, 7),
        "N14": (14, 7),
        "N15": (15, 7),
        "N16": (16, 7),
        "N17": (17, 7),
        "N18": (18, 7),
        "N19": (19, 7),
        "N20": (20, 7),
        "N21": (21, 7),
        "N22": (22, 7),
        "N23": (23, 7),
        "N24": (24, 7),
        "O12": (12, 8),
        "O13": (13, 8),
        "O14": (14, 8),
        "O15": (15, 8),
        "O16": (16, 8),
        "O17": (17, 8),
        "O18": (18, 8),
        "O19": (19, 8),
        "O20": (20, 8),
        "O21": (21, 8),
        "O22": (22, 8),
        "O23": (23, 8),
        "O24": (24, 8),
        "O25": (25, 8),
        "O26": (26, 8),
        "F14": (14, 9),
        "F15": (15, 9),
        "F16": (16, 9),
        "F17": (17, 9),
        "F18": (18, 9),
        "F19": (19, 9),
        "F20": (20, 9),
        "F21": (21, 9),
        "F22": (22, 9),
        "F23": (23, 9),
        "F24": (24, 9),
        "F25": (25, 9),
        "F26": (26, 9),
        "F27": (27, 9),
        "F28": (28, 9),
        "F29": (29, 9),
        "Ne16": (16, 10),
        "Ne17": (17, 10),
        "Ne18": (18, 10),
        "Ne19": (19, 10),
        "Ne20": (20, 10),
        "Ne21": (21, 10),
        "Ne22": (22, 10),
        "Ne23": (23, 10),
        "Ne24": (24, 10),
        "Ne25": (25, 10),
        "Ne26": (26, 10),
        "Ne27": (27, 10),
        "Ne28": (28, 10),
        "Ne29": (29, 10),
        "Ne30": (30, 10),
        "Ne31": (31, 10),
        "Ne32": (32, 10),
        "Na18": (18, 11),
        "Na19": (19, 11),
        "Na20": (20, 11),
        "Na21": (21, 11),
        "Na22": (22, 11),
        "Na23": (23, 11),
        "Na24": (24, 11),
        "Na25": (25, 11),
        "Na26": (26, 11),
        "Na27": (27, 11),
        "Na28": (28, 11),
        "Na29": (29, 11),
        "Na30": (30, 11),
        "Na31": (31, 11),
        "Na32": (32, 11),
        "Na33": (33, 11),
        "Na34": (34, 11),
        "Na35": (35, 11),
        "Mg20": (20, 12),
        "Mg21": (21, 12),
        "Mg22": (22, 12),
        "Mg23": (23, 12),
        "Mg24": (24, 12),
        "Mg25": (25, 12),
        "Mg26": (26, 12),
        "Mg27": (27, 12),
        "Mg28": (28, 12),
        "Mg29": (29, 12),
        "Mg30": (30, 12),
        "Mg31": (31, 12),
        "Mg32": (32, 12),
        "Mg33": (33, 12),
        "Mg34": (34, 12),
        "Mg35": (35, 12),
        "Mg36": (36, 12),
        "Mg37": (37, 12),
        "Al21": (21, 13),
        "Al22": (22, 13),
        "Al23": (23, 13),
        "Al24": (24, 13),
        "Al25": (25, 13),
        "Al26": (26, 13),
        "Al27": (27, 13),
        "Al28": (28, 13),
        "Al29": (29, 13),
        "Al30": (30, 13),
        "Al31": (31, 13),
        "Al32": (32, 13),
        "Al33": (33, 13),
        "Al34": (34, 13),
        "Al35": (35, 13),
        "Al36": (36, 13),
        "Al37": (37, 13),
        "Al38": (38, 13),
        "Al39": (39, 13),
        "Si22": (22, 14),
        "Si23": (23, 14),
        "Si24": (24, 14),
        "Si25": (25, 14),
        "Si26": (26, 14),
        "Si27": (27, 14),
        "Si28": (28, 14),
        "Si29": (29, 14),
        "Si30": (30, 14),
        "Si31": (31, 14),
        "Si32": (32, 14),
        "Si33": (33, 14),
        "Si34": (34, 14),
        "Si35": (35, 14),
        "Si36": (36, 14),
        "Si37": (37, 14),
        "Si38": (38, 14),
        "Si39": (39, 14),
        "Si40": (40, 14),
        "Si41": (41, 14),
        "Si42": (42, 14),
    }

    for name, azref in nucleus.items():
        az = pdg2AZ(name2pdg(name))
        assert azref == az
