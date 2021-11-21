# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:26:20 2018

@author: lamwa
"""

import math

with open('p099_base_exp.txt') as f:
    data = [[int(s) for s in l.strip().split(',')] for l in f.readlines()]

ans = 0
cur_max = 0.
for i, p in enumerate(data):
    cur = p[1] * math.log(p[0])
    if cur > cur_max:
        cur_max = cur
        ans = i + 1

print(ans)