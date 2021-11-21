# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 04:22:29 2018

@author: lamwa
"""

import math
import copy

RANGE = 1000000


def chain_len(n):
    ret = 0
    flag = dict()
    n_copy = copy.deepcopy(n)
    while True:
        if n_copy not in flag:
            flag[n_copy] = None
            ret += 1
        else:
            break
        n_copy = sum(math.factorial(int(c)) for c in list(str(n_copy)))
    return ret

ans = 0
for i in range(1, RANGE):
    if chain_len(i) == 60:
        ans += 1

print(ans)