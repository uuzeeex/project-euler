# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 03:51:42 2018

@author: lamwa
"""

import utils

RANGE = 1000000

phi = [0, 0] + [i for i in range(2, RANGE + 1)]
is_p = [False] * 2 + [True] * (RANGE - 1)

for i in range(2, RANGE + 1):
    if is_p[i]:
        phi[i] -= 1
        for j in range(2, RANGE // i + 1):
            is_p[i * j] = False
            phi[i * j] -= phi[i * j] // i

print(sum(phi))