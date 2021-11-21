# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 15:41:29 2018

@author: lamwa
"""

import itertools

co = [(x, y) for y in range(51) for x in range(51) if x + y != 0]

comb = list(itertools.combinations(co, 2))

def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

ans = 0

for p in comb:
    diff = (p[1][0] - p[0][0], p[1][1] - p[0][1])
    if dot(p[0], p[1]) == 0 or dot(p[0], diff) == 0 or dot(p[1], diff) == 0:
        ans += 1

print(ans)