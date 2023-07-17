import json

DATA = {}


def recover(variableName):
    global DATA
    with open("data.json", "r") as f:
        DATA = json.load(f)
    return DATA[variableName]


def backup(varName, var):
    global DATA
    DATA[varName] = var
    with open("data.json", "w") as f:
        json.dump(DATA, f)
