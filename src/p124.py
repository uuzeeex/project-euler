# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:31:39 2018

@author: lamwa
"""

N = 100000

rads = [1] * (N + 1)

for i in range(1, N + 1):
    if rads[i] == 1:
        for j in range(1, N // i + 1):
            rads[i * j] *= i

t = list(zip([i for i in range(1, N + 1)], rads[1 :]))
s = sorted(t, key=lambda x: (x[1], x[0]))
print(s[9999][0])