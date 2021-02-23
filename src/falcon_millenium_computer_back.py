import json


def read_file(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

