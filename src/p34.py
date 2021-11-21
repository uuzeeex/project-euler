# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 08:02:10 2018

@author: lamwa
"""

import copy

def fac(n):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

def cur(n):
    n_copy = copy.deepcopy(n)
    s = 0
    while n_copy > 0:
        s += fac(n_copy % 10)
        n_copy //= 10
    return s == n

ans = 0
for i in range(3, 10000000):
    if cur(i):
        ans += i

print(ans)