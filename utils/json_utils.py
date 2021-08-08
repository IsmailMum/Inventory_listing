import json

def read_master(file = "master.json"):
    with open(file) as file:
        data = json.load(file)
    return data

def read_counts(file = "counts.json"):
    with open(file) as file:
        data = json.load(file)
    return data