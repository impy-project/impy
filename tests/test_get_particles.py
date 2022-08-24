from impy.kinematics import _FromParticleName


def test_get_pdg():
    common_particles = {
        "d": 1,
        "u": 2,
        "s": 3,
        "c": 4,
        "b": 5,
        "t": 6,
        "e-": 11,
        "e+": -11,
        "nu(e)": 12,
        "nu(e)~": -12,
        "mu-": 13,
        "mu+": -13,
        "nu(mu)": 14,
        "nu(mu)~": -14,
        "tau-": 15,
        "tau+": -15,
        "nu(tau)": 16,
        "nu(tau)~": -16,
        "g": 21,
        "gamma": 22,
        "Z0": 23,
        "W+": 24,
        "W-": -24,
        "H0": 25,
        "pi0": 111,
        "rho(770)0": 113,
        "a(2)(1320)0": 115,
        "rho(3)(1690)0": 117,
        "a(4)(1970)0": 119,
        "K(L)0": 130,
        "pi+": 211,
        "pi-": -211,
        "rho(770)+": 213,
        "rho(770)-": -213,
        "a(2)(1320)+": 215,
        "a(2)(1320)-": -215,
        "rho(3)(1690)+": 217,
        "rho(3)(1690)-": -217,
        "a(4)(1970)+": 219,
        "a(4)(1970)-": -219,
        "eta": 221,
        "omega(782)": 223,
        "f(2)(1270)": 225,
        "omega(3)(1670)": 227,
        "f(4)(2050)": 229,
        "K(S)0": 310,
        "K0": 311,
        "K~0": -311,
        "K*(892)0": 313,
        "K*(892)~0": -313,
        "K(2)*(1430)0": 315,
        "K(2)*(1430)~0": -315,
        "K(3)*(1780)0": 317,
        "K(3)*(1780)~0": -317,
        "K(4)*(2045)0": 319,
        "K(4)*(2045)~0": -319,
        "K+": 321,
        "K-": -321,
        "K*(892)+": 323,
        "K*(892)-": -323,
        "K(2)*(1430)+": 325,
        "K(2)*(1430)-": -325,
        "K(3)*(1780)+": 327,
        "K(3)*(1780)-": -327,
        "K(4)*(2045)+": 329,
        "K(4)*(2045)-": -329,
        "eta'(958)": 331,
        "phi(1020)": 333,
        "f(2)'(1525)": 335,
        "phi(3)(1850)": 337,
        "D+": 411,
        "D-": -411,
        "D*(2010)+": 413,
        "D*(2010)-": -413,
        "D(2)*(2460)+": 415,
        "D(2)*(2460)-": -415,
        "D0": 421,
        "D~0": -421,
        "D*(2007)0": 423,
        "D*(2007)~0": -423,
        "D(2)*(2460)0": 425,
        "D(2)*(2460)~0": -425,
        "D(s)+": 431,
        "D(s)-": -431,
        "D(s)*+": 433,
        "D(s)*-": -433,
        "D(s2)*(2573)+": 435,
        "D(s2)*(2573)-": -435,
        "eta(c)(1S)": 441,
        "J/psi(1S)": 443,
        "chi(c2)(1P)": 445,
        "B0": 511,
        "B~0": -511,
        "B*0": 513,
        "B*~0": -513,
        "B(2)*(5747)0": 515,
        "B(2)*(5747)~0": -515,
        "B+": 521,
        "B-": -521,
        "B*+": 523,
        "B*-": -523,
        "B(2)*(5747)+": 525,
        "B(2)*(5747)-": -525,
        "B(s)0": 531,
        "B(s)~0": -531,
        "B(s)*0": 533,
        "B(s)*~0": -533,
        "B(s2)*(5840)0": 535,
        "B(s2)*(5840)~0": -535,
        "B(c)+": 541,
        "B(c)-": -541,
        "Upsilon(1S)": 553,
        "chi(b2)(1P)": 555,
        "(dd)(1)": 1103,
        "(dd)(1)~": -1103,
        "Delta(1620)-": 1112,
        "Delta(1620)~+": -1112,
        "Delta(1232)-": 1114,
        "Delta(1232)~+": -1114,
        "Delta(1905)-": 1116,
        "Delta(1905)~+": -1116,
        "Delta(1950)-": 1118,
        "Delta(1950)~+": -1118,
        "Delta(1620)0": 1212,
        "Delta(1620)~0": -1212,
        "N(1520)0": 1214,
        "N(1520)~0": -1214,
        "Delta(1905)0": 1216,
        "Delta(1905)~0": -1216,
        "N(2190)0": 1218,
        "N(2190)~0": -1218,
        "Delta(1232)0": 2114,
        "Delta(1232)~0": -2114,
        "N(1675)0": 2116,
        "N(1675)~0": -2116,
        "Delta(1950)0": 2118,
        "Delta(1950)~0": -2118,
        "Delta(1620)+": 2122,
        "Delta(1620)~-": -2122,
        "N(1520)+": 2124,
        "N(1520)~-": -2124,
        "Delta(1905)+": 2126,
        "Delta(1905)~-": -2126,
        "N(2190)+": 2128,
        "N(2190)~-": -2128,
        "(uu)(1)": 2203,
        "(uu)(1)~": -2203,
        "p": 1000010010,
        "p~": -1000010010,
        "Delta(1232)+": 2214,
        "Delta(1232)~-": -2214,
        "N(1675)+": 2216,
        "N(1675)~-": -2216,
        "Delta(1950)+": 2218,
        "Delta(1950)~-": -2218,
        "Delta(1620)++": 2222,
        "Delta(1620)~--": -2222,
        "Delta(1232)++": 2224,
        "Delta(1232)~--": -2224,
        "Delta(1905)++": 2226,
        "Delta(1905)~--": -2226,
        "Delta(1950)++": 2228,
        "Delta(1950)~--": -2228,
        "(sd)(0)": 3101,
        "(sd)(0)~": -3101,
        "(sd)(1)": 3103,
        "(sd)(1)~": -3103,
        "Sigma-": 3112,
        "Sigma~+": -3112,
        "Sigma(1385)-": 3114,
        "Sigma(1385)~+": -3114,
        "Sigma(1775)-": 3116,
        "Sigma(1775)~+": -3116,
        "Sigma(2030)-": 3118,
        "Sigma(2030)~+": -3118,
        "Lambda": 3122,
        "Lambda~": -3122,
        "Lambda(1520)": 3124,
        "Lambda(1520)~": -3124,
        "Lambda(1820)": 3126,
        "Lambda(1820)~": -3126,
        "Lambda(2100)": 3128,
        "Lambda(2100)~": -3128,
        "(su)(0)": 3201,
        "(su)(0)~": -3201,
        "photon": 22,
        "Higgs": 25,
        "proton": 2212,
        "antiproton": -2212,
        "neutron": 2112,
        "antineutron": -2112,
        "e_minus": 11,
        "e_plus": -11,
        "nu_e": 12,
        "nu_e_bar": -12,
        "mu_minus": 13,
        "mu_plus": -13,
        "nu_mu": 14,
        "nu_mu_bar": -14,
        "tau_minus": 15,
        "tau_plus": -15,
        "nu_tau": 16,
        "nu_tau_bar": -16,
        "taup_minus": 17,
        "taup_plus": -17,
        "nu_taup": 18,
        "nu_taup_bar": -18,
        "Z_0": 23,
        "W_plus": 24,
        "W_minus": -24,
        "H_0": 25,
        "pi_0": 111,
    }

    for name, pdg in common_particles.items():
        pdg_res = _FromParticleName._get_pdg(name)
        assert pdg_res == pdg, "For '{0}' expected pdg = {1}, but received {2}".format(
            name, pdg, pdg_res
        )


def test_get_AZ():
    nucleus = {
        "n": (1, 0),
        "p": (1, 1),
        "D2": (2, 1),
        "T3": (3, 1),
        "H4": (4, 1),
        "H5": (5, 1),
        "H6": (6, 1),
        "He3": (3, 2),
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

    for name, az in nucleus.items():
        az_res = _FromParticleName._get_AZ(name)
        assert az_res == az, "For '{0}' expected az = {1}, but received {2}".format(
            name, az, az_res
        )


def test_composite_target():
    from impy.kinematics import CompositeTarget

    air = CompositeTarget(
        [
            ("N14", 2 * 0.78084, "Nitrogen"),
            ((16, 8), 2 * 0.20946, "Oxygen"),
            ("Ar40", 0.00934),
            ("O16", 0.004, "Oxygen(Vapor)"),
            ("proton", 2 * 0.004, "Hydrogen(Vapor)"),
        ],
        "Air",
    )

    seed_for_outcome = 321
    expected_az = [
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (16, 8),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (40, 18),
        (14, 7),
        (16, 8),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (16, 8),
        (16, 8),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (40, 18),
        (16, 8),
        (14, 7),
        (16, 8),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
        (14, 7),
        (16, 8),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (14, 7),
        (16, 8),
    ]
    air.set_rng_seed(seed_for_outcome)

    outcome_az = []
    for _ in range(len(expected_az)):
        outcome_az.append(air.get_random_AZ())

    assert outcome_az == expected_az, "get_random_AZ(): outcome != expected"
