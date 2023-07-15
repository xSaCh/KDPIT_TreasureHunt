RIDDLES = [
    ["T1R1", "T1R2", "T1R3", "T1R4", "T1R5", "T1R6"],
    ["T2R1", "T2R2", "T2R3", "T2R4", "T2R5", "T2R6"],
    ["T3R1", "T3R2", "T3R3", "T3R4", "T3R5", "T3R6"],
    ["T4R1", "T4R2", "T4R3", "T4R4", "T4R5", "T4R6"],
    ["T5R1", "T5R2", "T5R3", "T5R4", "T5R5", "T5R6"],
    ["T6R1", "T6R2", "T6R3", "T6R4", "T6R5", "T6R6"],
]

CODE_TO_RD = {
    "TCHJ0PB": "10",
    "UM68LWV": "11",
    "2I9QVVI": "12",
    "TAUQ1UM": "13",
    "N3MBJJG": "14",
    "JOHFCFW": "15",
    "8E231TC": "20",
    "I1U7RKA": "21",
    "89QCX1D": "22",
    "WAYJE5D": "23",
    "T9Z4CSP": "24",
    "B9M51EW": "25",
    "SXA04WP": "30",
    "VOB1S0I": "31",
    "3J6TMM3": "32",
    "0HI7MOK": "33",
    "UTS07GP": "34",
    "BYWR5TM": "35",
    "W5SBCSC": "40",
    "6CU1EOD": "41",
    "GUC2VUI": "42",
    "QULM68C": "43",
    "9UPCJLQ": "44",
    "74IQ1ZF": "45",
    "MS44C83": "50",
    "VQC6T94": "51",
    "IKWHA9V": "52",
    "98HW14H": "53",
    "DQPFTG3": "54",
    "CZ2H2VV": "55",
    "ZUOK859": "60",
    "JAITXPU": "61",
    "5AXP5JP": "62",
    "ULKN4E8": "63",
    "BW3QMHW": "64",
    "X7K9KD7": "65",
}


def codeToTeam(code):
    if code not in CODE_TO_RD:
        return -1

    return CODE_TO_RD[code]
