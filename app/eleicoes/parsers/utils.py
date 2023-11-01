import requests 
import json

def load(file):
    if "http" in file:
        data = requests.get(file).json()
    else:
        with open(file) as f:
            data = json.load(f)
    return data