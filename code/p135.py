# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:13:28 2018

@author: lamwa
"""

SUP = 1000000

cnt = [0] * SUP

for k in range(2, SUP):
    for i in range(1, SUP // k + (SUP % k != 0)):
        if (i + k) % 4 == 0 and (i + k) // 4 < k:
            a = (i + k) // 4
            cnt[k * i] += 1

ans = sum(c == 10 for c in cnt)
