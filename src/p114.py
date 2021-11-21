# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:19:20 2018

@author: lamwa
"""

N = 50

f = [[[0] * (N + 1) for _ in range(2)] for _ in range(N)]

f[0][0][0], f[0][1][1] = 1, 1

for i in range(1, N):
    f[i][0][0] = f[i - 1][0][0] + sum(f[i - 1][1][3 : i + 1])
    f[i][1][1] = f[i - 1][0][0]
    for k in range(2, i + 2):
        f[i][1][k] = f[i - 1][1][k - 1]

ans = f[N - 1][0][0] + sum(f[N - 1][1][3 :])
print(ans)