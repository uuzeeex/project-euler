# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:30:00 2018

@author: lamwa
"""

import math

def d(n):
    res = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if i * i == n:
            res += i
        elif n % i == 0:
            res += i + (n // i)
    return res

ans = 0
for i in range(1, 10000):
    j = d(i)
    if i != j and d(j) == i:
        ans += i

print(ans)