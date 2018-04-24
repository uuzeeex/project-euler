# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:35:42 2018

@author: lamwa
"""

r = dict()

def power(a, b):
    p = 1
    for i in range(b):
        p *= a
    return p

ans = 0

for a in range(2, 101):
    for b in range(2, 101):
        p = power(a, b)
        if p not in r:
            r[p] = None
            ans += 1

print(ans)