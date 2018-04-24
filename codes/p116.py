# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:53:31 2018

@author: lamwa
"""

def cal(n, l):
    f = [[0] * (l + 1) for _ in range(n)]
    f[0][0], f[0][1] = 1, 1
    for i in range(1, n):
        f[i][0] = f[i - 1][0] + f[i - 1][l]
        f[i][1] = f[i][0]
        for j in range(2, l + 1):
            f[i][j] = f[i - 1][j - 1]
    return f[n - 1][0] + f[n - 1][l] - 1

print(sum(cal(50, i) for i in range(2, 5)))