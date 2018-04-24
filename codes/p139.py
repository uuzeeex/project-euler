# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 20:17:18 2018

@author: lamwa
"""

import math

RANGE = 100000000

ans = 0

for m in range(2, int(math.sqrt(RANGE / 2))):
    for n in range(m - 1, 0, -2):
        if math.gcd(m, n) == 1:
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            l = 2 * m * (m + n)
            if c % abs(a - b) == 0:
                ans += RANGE // l - (RANGE % l == 0)

print(ans)