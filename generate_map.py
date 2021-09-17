#!/usr/bin/python3
import random

_map = [3, 4, 5, 7, 8, 9]

def generate_map():
    e = random.choice(_map)
    if e >= 3 and e <= 5:
        n = _map[::-1][0:3][_map[0:3].index(e)]
    else:
        n = _map[0:3][_map[::-1][0:3].index(e)]
    return {"Extended": e, "Normal": n}
