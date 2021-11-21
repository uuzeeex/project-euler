# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:00:25 2018

@author: lamwa
"""

M, N = 43, 47

f = [[0] * (N + 1) for _ in range(M + 1)]
b = [[False] * (N + 1) for _ in range(M + 1)]

def cal_oblique(m, squ):
    ret = 0
    for i in range(1,  2 * m):
        ret += i * (2 * m - i)
    if squ: ret -= m
    return ret

def count_oblique(m, n):
    if m > n:
        m, n = n, m
    if not b[m][n]:
        f[m][n] = cal_oblique(m, m == n) + count_oblique(m, n - 1)
        b[m][n] = True
    return f[m][n]

def count_hv(m, n):
    ret = 0
    for i in range(m):
        for j in range(n):
            ret += (m - i) * (n - j)
    return ret

f[1][1] = 0
b[1][1] = True
ans = 0
for i in range(1, M + 1):
    for j in range(1, N + 1):
        ans += count_oblique(i, j) + count_hv(i, j)
print(ans)