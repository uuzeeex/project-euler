# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:35:37 2018

@author: lamwa
"""

import utils

RANGE = 100

_, p_list = utils.sieve(RANGE)
n = len(p_list)

f = [[0] * (n + 1) for _ in range(RANGE + 1)]
for i in range(n):
    f[p_list[i]][i] = 1
for i in range(2, RANGE + 1):
    j = 0
    while j < n and p_list[j] < i:
        k = 0
        while k < n and p_list[k] <= min(p_list[j], i - p_list[j]):
            f[i][j] += f[i - p_list[j]][k]
            k += 1
        j += 1
    if sum(f[i]) > 5000:
        print(i)
        break