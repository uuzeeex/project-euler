# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:55:05 2018

@author: lamwa
"""

import numpy as np

with open('p067_triangle.txt') as f:
    n = max([len(line.split()) for line in f.readlines()])

with open('p067_triangle.txt') as f:
    tri = np.array([([int(i) for i in line.split()] + [0] * (n - len(line.split()))) for line in f.readlines()])

f = np.zeros(tri.shape, dtype=int)

f[0, 0] = tri[0, 0]
for i in range(1, n):
    for j in range(i + 1):
        f[i, j] = tri[i, j]
        if j == 0:
            f[i, j] += f[i - 1, j]
        elif j == i:
            f[i, j] += f[i - 1, j - 1]
        else:
            f[i, j] += max(f[i - 1, j], f[i - 1, j - 1])

print(np.max(f[n - 1]))