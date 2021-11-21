# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:28:38 2018

@author: lamwa
"""

import math

RANGE = 1000

n = 1
d = 1
cnt = 0
for i in range(RANGE):
    n += 2 * d
    d = n - d
    n //= math.gcd(n, d)
    d //= math.gcd(n, d)
    if len(str(n)) > len(str(d)):
        cnt += 1

print(cnt)