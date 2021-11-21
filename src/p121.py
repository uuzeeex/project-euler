# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:07:55 2018

@author: lamwa
"""

N = 15

f = [[0] * (i + 1) for i in range(N + 1)]

f[0][0] = 1.

for i in range(1, N + 1):
    f[i][0] = f[i - 1][0] * (i / (1 + i))
    for j in range(1, i):
        f[i][j] = f[i - 1][j - 1] * (1 / (1 + i)) + f[i - 1][j] * (i / (1 + i))
    f[i][i] = f[i - 1][i - 1] * (1 / (1 + i))

ans = int(1 / sum(f[N][N // 2 + 1 :]))

print(ans)