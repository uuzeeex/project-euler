# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:35:28 2018

@author: lamwa
"""

import numpy as np

m = 100
n = 100

B = 2000000

ans = 0
cur_min = float('inf')

for m in range(100):
    for n in range(100):
        r = np.array([m - i for i in range(m)])
        c = np.array([n - i for i in range(n)])
        E = np.ones((m, n), dtype=int)
        cur = abs(r.dot(E).dot(c) - B)
        if cur < cur_min:
            cur_min = cur
            ans = m * n

print(ans)