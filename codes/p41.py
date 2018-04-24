# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:04:46 2018

@author: lamwa
"""

import numpy as np
import itertools

RANGE = 8000000

p = np.ones(RANGE, dtype=bool)

p[0] = False
p[1] = False

for i in range(2, RANGE):
    if p[i]:
        for j in range(i, (RANGE - 1) // i + 1):
            p[i * j] = False

def max_pan():
    for i in range(7, 0, -1):
        for per in list(itertools.permutations([str(d) for d in range(i, 0, -1)])):
            if p[int(''.join(per))]:
                return int(''.join(per))

print(max_pan())