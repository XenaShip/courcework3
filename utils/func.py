import json


def unpacking():
    file = open("operations.json")
    inf = json.load(file)
    return inf
