# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:43:41 2018

@author: lamwa
"""

import copy

MAX = 1000000

def check(n):
    s = 0
    n_copy = copy.deepcopy(n)
    while n > 0:
        u = n % 10
        s += u * u * u * u * u
        n //= 10
    return s == n_copy

ans = 0
for i in range(MAX):
    if check(i):
        ans += i

print(ans - 1)