# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:10:05 2018

@author: lamwa
"""

with open('p083_matrix.txt') as f:
    mat = [[int(s) for s in l.strip().split(',')] for l in f.readlines()]

m, n = len(mat), len(mat[0])

f = [[[float('inf')] * n for _ in range(m)] for _ in range(m * n)]

f[0][0][0] = mat[0][0]

for t in range(1, m * n):
    for i in range(m):
        for j in range(n):
            if i > 0:
                f[t][i][j] = min(f[t][i][j], f[t - 1][i - 1][j])
            if j < n - 1:
                f[t][i][j] = min(f[t][i][j], f[t - 1][i][j + 1])
            if i < m - 1:
                f[t][i][j] = min(f[t][i][j], f[t - 1][i + 1][j])
            if j > 0:
                f[t][i][j] = min(f[t][i][j], f[t - 1][i][j - 1])
            f[t][i][j] += mat[i][j]

print(min(f[t][m - 1][n - 1] for t in range(m * n)))