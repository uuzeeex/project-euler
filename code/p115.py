# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:44:56 2018

@author: lamwa
"""

N = 200
TH = 1000000

f = [[[0] * (N + 1) for _ in range(2)] for _ in range(N)]

f[0][0][0], f[0][1][1] = 1, 1

i = 1
while True:
    f[i][0][0] = f[i - 1][0][0] + sum(f[i - 1][1][50 : i + 1])
    f[i][1][1] = f[i - 1][0][0]
    for k in range(2, i + 2):
        f[i][1][k] = f[i - 1][1][k - 1]
    cur = f[i - 1][0][0] + sum(f[i - 1][1][50 :])
    if cur > TH:
        print(i)
        break
    i += 1
