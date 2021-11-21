# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:51:56 2018

@author: lamwa
"""

import numpy as np

coins = np.array([0, 1, 2, 5, 10, 20, 50, 100, 200])

f = np.zeros((201, 9))
f[0, 0] = 1
for i in range(1, 201):
    for j in range(1, 9):
        if i >= coins[j]:
            f[i, j] = 0
            for k in range(j + 1):
                f[i, j] += f[i - coins[j]][k]

print(sum(f[200]))