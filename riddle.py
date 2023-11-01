RIDDLES = [
    ["T1R1", "T1R2", "T1R3", "T1R4", "T1R5", "T1R6"],
    ["T2R1", "T2R2", "T2R3", "T2R4", "T2R5", "T2R6"],
    ["T3R1", "T3R2", "T3R3", "T3R4", "T3R5", "T3R6"],
    ["T4R1", "T4R2", "T4R3", "T4R4", "T4R5", "T4R6"],
    ["T5R1", "T5R2", "T5R3", "T5R4", "T5R5", "T5R6"],
    ["T6R1", "T6R2", "T6R3", "T6R4", "T6R5", "T6R6"],
]

CODE_TO_RD = {
    "TCHJ0PB": "11",
    "UM68LWV": "12",
    "2I9QVVI": "13",
    "TAUQ1UM": "14",
    "N3MBJJG": "15",
    "JOHFCFW": "16",
    "8E231TC": "21",
    "I1U7RKA": "22",
    "89QCX1D": "23",
    "WAYJE5D": "24",
    "T9Z4CSP": "25",
    "B9M51EW": "26",
    "SXA04WP": "31",
    "VOB1S0I": "32",
    "3J6TMM3": "33",
    "0HI7MOK": "34",
    "UTS07GP": "35",
    "BYWR5TM": "36",
    "W5SBCSC": "41",
    "6CU1EOD": "42",
    "GUC2VUI": "43",
    "QULM68C": "44",
    "9UPCJLQ": "45",
    "74IQ1ZF": "46",
    "MS44C83": "51",
    "VQC6T94": "52",
    "IKWHA9V": "53",
    "98HW14H": "54",
    "DQPFTG3": "55",
    "CZ2H2VV": "56",
    "ZUOK859": "61",
    "JAITXPU": "62",
    "5AXP5JP": "63",
    "ULKN4E8": "64",
    "BW3QMHW": "65",
    "X7K9KD7": "66",
}

# CODE_TO_RD = {
#     "10": "11",
#     "11": "12",
#     "12": "13",
#     "13": "14",
#     "14": "15",
#     "15": "16",
#     "20": "21",
#     "21": "22",
#     "22": "23",
#     "23": "24",
#     "24": "25",
#     "25": "26",
#     "30": "31",
#     "31": "32",
#     "32": "33",
#     "33": "34",
#     "34": "35",
#     "35": "36",
#     "40": "41",
#     "41": "42",
#     "42": "43",
#     "43": "44",
#     "44": "45",
#     "45": "46",
#     "50": "51",
#     "51": "52",
#     "52": "53",
#     "53": "54",
#     "54": "55",
#     "55": "56",
#     "60": "61",
#     "61": "62",
#     "62": "63",
#     "63": "64",
#     "64": "65",
#     "65": "66",
# }


def codeToTeam(code):
    if code not in CODE_TO_RD:
        return -1

    return CODE_TO_RD[code]
