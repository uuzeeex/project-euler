# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:53:48 2018

@author: lamwa
"""

import utils

RANGE = 7100
N = 50000000

_, p_list = utils.sieve(RANGE)

cur = 0
tri = set()

for p1 in p_list:
    cur += p1 * p1
    if cur > N:
        break
    for p2 in p_list:
        cur += p2 * p2 * p2
        if cur > N:
            cur -= p2 * p2 * p2
            break
        for p3 in p_list:
            cur += p3 * p3 * p3 * p3
            if cur > N:
                cur -= p3 * p3 * p3 * p3
                break
            tri.add(cur)
            cur -= p3 * p3 * p3 * p3
        cur -= p2 * p2 * p2
    cur -= p1 * p1

print(len(tri))