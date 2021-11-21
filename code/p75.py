# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:31:06 2018

@author: lamwa
"""

import math

RANGE = 1500000

cnt = [0] * (RANGE + 1)

for m in range(2, int(math.sqrt(RANGE / 2))):
    for n in range(m - 1, 0, -2):
        if math.gcd(m, n) == 1:
            l = 2 * m * (m + n)
            for i in range(1, RANGE // l + 1):
                cnt[l * i] += 1

print(sum(1 for c in cnt if c == 1))