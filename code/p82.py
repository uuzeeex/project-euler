# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:38:20 2018

@author: lamwa
"""

import copy

with open('p082_matrix.txt') as f:
    mat = [[int(s) for s in l.strip().split(',')] for l in f.readlines()]

m, n = len(mat), len(mat[0])

s = copy.deepcopy(mat)

for i in range(1, m):
    for j in range(0, n):
        s[i][j] += s[i - 1][j]

f = [[[0] * m for _ in range(m)] for _ in range(n)]

for j in range(0, m):
    for k in range(0, m):
        _j = min(j, k)
        _k = max(j, k)
        f[0][j][k] = s[_k][0] - s[_j][0] + mat[_j][0]

for i in range(1, n):
    for j in range(0, m):
        for k in range(0, m):
            _j = min(j, k)
            _k = max(j, k)
            f[i][j][k] = min(f[i - 1][l][j] for l in range(0, m)) + s[_k][i] - s[_j][i] + mat[_j][i]

print(min(f[n - 1][j][k] for k in range(0, m) for j in range(0, m)))