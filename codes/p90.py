# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 23:05:26 2018

@author: lamwa
"""

import itertools

c = list(itertools.combinations([i for i in range(10)], 6))

sqrs = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]

def can(c, d):
    if d  == 6 or d == 9:
        return 6 in c or 9 in c
    return d in c

def check(c1, c2):
    for sqr in sqrs:
        if can(c1, sqr[0]) and can(c2, sqr[1]):
            continue
        if can(c2, sqr[0]) and can(c1, sqr[1]):
            continue
        return False
    return True

ans = 0

for c1 in c:
    for c2 in c:
        if c1 <= c2:
            if check(c1, c2):
                ans += 1