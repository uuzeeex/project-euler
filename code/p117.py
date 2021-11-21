# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 22:29:45 2018

@author: lamwa
"""

def cal(n, l, r):
    f = [[0] * (r + 1) for _ in range(n)]
    f[0][0], f[0][1] = 1, 1
    for i in range(1, n):
        f[i][0] = f[i - 1][0] + sum(f[i - 1][l : r + 1])
        f[i][1] = f[i][0]
        for j in range(2, r + 1):
            f[i][j] = f[i - 1][j - 1]
    return f[n - 1][0] + sum(f[n - 1][l : r + 1])

print(cal(50, 2, 4))