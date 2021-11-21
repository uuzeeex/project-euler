# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 04:13:37 2018

@author: lamwa
"""

import math

ans = 0

for d in range(4, 12001):
    s = int(math.ceil(d / 3))
    t = int(math.floor(d / 2))
    for n in range(s, t + 1):
        if math.gcd(n, d) == 1:
            ans += 1

print(ans)