# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:56:39 2018

@author: lamwa
"""

import utils
import math

N = 120000

mapping = [set() for _ in range(N)]

for p in range(1, N):
    for q in range(1, min(p, N - p) + 1):
        b = p * p + q * q + p * q
        if utils.is_square(b):
            mapping[p].add(q)

ans_set = set()
for p in range(1, N):
    for q in mapping[p]:
        for r in mapping[q]:
            if p + q + r <= N and r in mapping[p]:
                ans_set.add(p + q + r)
ans = sum(ans_set)
print(ans)