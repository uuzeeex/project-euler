# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 23:23:39 2018

@author: lamwa
"""

import numpy as np

RANGE = 100

f = np.zeros((RANGE + 1, RANGE + 1), dtype=int)
for i in range(1, RANGE + 1):
    f[i, i] = 1
for i in range(2, RANGE + 1):
    for j in range(1, i):
        for k in range(1, min(j, i - j) + 1):
            f[i, j] += f[i - j, k]

print(np.sum(f[RANGE][: RANGE]))