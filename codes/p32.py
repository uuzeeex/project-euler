# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:08:30 2018

@author: lamwa
"""

import itertools

pers = list(itertools.permutations([i + 1 for i in range(9)]))

flag = dict()

def correct(p, m, e):
    mul1 = 0
    for i in range(m + 1):
        mul1 = mul1 * 10 + p[i]
    mul2 = 0
    for i in range(m + 1, e + 1):
        mul2 = mul2 * 10 + p[i]
    prod = 0
    for i in range(e + 1, 9):
        prod = prod * 10 + p[i]
    return mul1 * mul2 == prod, prod

for p in pers:
    for m in range(7):
        for e in range(m + 1, 8):
            c, prod = correct(p, m, e)
            if c:
                flag[prod] = None

ans = 0
for key in flag:
    ans += key

print(ans)