# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:45:04 2018

@author: lamwa
"""

import utils

SUP = 100000

def cycle_len(mod):
    rems = set()
    n = 1
    while n not in rems:
        rems.add(n)
        n = (n * 10 + 1) % mod
    return len(rems)

def check(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    return n == 1

ans = 0
for i in range(2, SUP):
    if utils.miller_rabin(i):
        if i == 2 or i == 5 or not check(cycle_len(i)):
            ans += i

print(ans)