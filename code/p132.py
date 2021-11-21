# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:21:31 2018

@author: lamwa
"""

import utils

N = 10 ** 9
RANGE = 10 ** 6

_, p_list = utils.sieve(RANGE)

def cycle_len(mod):
    rems = set()
    n = 1
    while n not in rems:
        rems.add(n)
        n = (n * 10 + 1) % mod
    return len(rems)

cnt, ans = 0, 0
for p in p_list:
    if p != 2 and p != 5:
        if N % cycle_len(p) == 0:
            ans += p
            cnt += 1
            if cnt == 40:
                break

print(ans)