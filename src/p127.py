# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:42:37 2018

@author: lamwa
"""

import math

N = 120000

rads = [1] * (N + 1)

for i in range(1, N + 1):
    if rads[i] == 1:
        for j in range(1, N // i + 1):
            rads[i * j] *= i

t = list(zip([i for i in range(1, N + 1)], rads[1 :]))
s = sorted(t, key=lambda x: (x[1], x[0]))

ans = 0
for c in range(3, N):
    for a, rada in s:
        if rada * rads[c] <= c // 2:
            if a >= c - a:
                continue
            b = c - a
            if rada * rads[b] * rads[c] < c and math.gcd(a, b) == 1:
                ans += c
        else:
            break