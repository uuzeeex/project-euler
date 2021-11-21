# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 00:12:23 2018

@author: lamwa
"""

p = [1, 1]

def gen(k):
    return k * (3 * k - 1) // 2

while True:
    n = len(p)
    k = 1
    sign = 1
    new = 0
    while gen(k) <= n:
        new += sign * p[n - gen(k)]
        if k > 0:
            k = -k
        else:
            k = -k + 1
            sign = -sign
    p.append(new)
    if new % 1000000 == 0:
        print(n)
        break