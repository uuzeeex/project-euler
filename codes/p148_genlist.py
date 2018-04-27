# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:45:19 2018

@author: lamwa
"""

RANGE = 100

C = [[1]]

for i in range(1, RANGE):
    C.append([C[-1][0]])
    for j in range(1, i):
        C[-1].append(C[-2][j - 1] + C[-2][j])
    C[-1].append(C[-2][-1])

a = []
for r in C:
    cnt = 0
    for c in r:
        if c % 7 != 0:
            cnt += 1
    a.append(cnt)

print(a)