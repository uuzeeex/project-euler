# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:40:48 2018

@author: lamwa
"""

dps = set()

n = 2
while len(dps) < 40:
    if n == 10:
        n += 1
    i = 1
    while True:
        s = sum(int(d) for d in str(n ** i))
        if n ** i < 10:
            i += 1
            continue
        if s == n:
            dps.add(n ** i)
        if s > n + 100:
            break
        i += 1
    n += 1

print(sorted(dps)[29])