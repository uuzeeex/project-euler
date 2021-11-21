# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:30:34 2018

@author: lamwa
"""

import math

seq = []

for i in range(66, 1, -2):
    seq += [1, i, 1]

seq.append(2)

a = 1
b = 1
for si in seq[1 :]:
    na = b + a * si
    b = a
    a = na
    a //= math.gcd(a, b)
    b //= math.gcd(a, b)

print(sum([int(c) for c in str(a)]))