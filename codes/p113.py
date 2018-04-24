# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 19:58:03 2018

@author: lamwa
"""

N = 100

f1 = [[0] * 10 for _ in range(N)]
f2 = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    f1[0][i], f2[0][i] = 1, 1

for i in range(1, N):
    for j in range(10):
        f1[i][j] += sum(f1[i - 1][k] for k in range(j + 1))
        f2[i][j] += sum(f2[i - 1][k] for k in range(j, 10))

ans = 0
for i in range(0, N):
    ans += sum(f1[i]) + sum(f2[i]) - 9
print(ans)