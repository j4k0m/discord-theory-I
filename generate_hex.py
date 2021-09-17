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

def generate():
    c = generate_map()
    ex, no = c["Extended"], c["Normal"]
    _chars = random.sample(range(128,255), ex)
    _chars.extend(random.sample(range(1,126), no))
    random.shuffle(_chars)
    return " ".join(list(map(hex ,_chars)))

print(generate())
