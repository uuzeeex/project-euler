# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:26:04 2018

@author: lamwa
"""

import numpy as np

ddx = 8
dx = np.array([2, 4, 6, 8])
x = np.array([1, 1, 1, 1])

ans = 1

for i in range(500):
    x += dx
    ans += sum(x)
    dx += ddx

print(ans)