# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:06:48 2018

@author: lamwa
"""

with open('p081_matrix.txt') as f:
    mat = [[int(s) for s in l.strip().split(',')] for l in f.readlines()]

m, n = len(mat), len(mat[0])

f = [[0] * n for _ in range(m)]

f[0][0] = mat[0][0]

for i in range(1, m):
    f[i][0] = f[i - 1][0] + mat[i][0]

for j in range(1, n):
    f[0][j] = f[0][j - 1] + mat[0][j]

for i in range(1, m):
    for j in range(1, n):
        f[i][j] = min(f[i - 1][j], f[i][j - 1]) + mat[i][j]

print(f[m - 1][n - 1])