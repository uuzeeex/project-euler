# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:11:40 2018

@author: lamwa
"""

import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def max_n(a, b):
    n = 0
    while prime(n * n + a * n + b):
        n += 1
    return n

cur_max = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        cur = max_n(a, b)
        if cur > cur_max:
            cur_max = cur
            ans = (a, b)

print(ans[0] * ans[1])