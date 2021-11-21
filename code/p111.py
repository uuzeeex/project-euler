# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:58:40 2018

@author: lamwa
"""

import utils
import itertools

N = 10

def dfs(d, flag, cur, i):
    if (i == N):
        if utils.miller_rabin(cur):
            return cur
        return 0
    if flag[i]:
        return dfs(d, flag, cur * 10 + d, i + 1)
    s = 1 if i == 0 else 0
    ret = 0
    for k in range(s, 10):
        ret += dfs(d, flag, cur * 10 + k, i + 1)
    return ret

ans = 0
for d in range(10):
    m = 10 if d > 0 else 9
    while m > 0:
        if d > 0:
            combs = itertools.combinations([i for i in range(10)], m)
        else:
            combs = itertools.combinations([i for i in range(1, 10)], m)
        s = 0
        for comb in combs:
            s += dfs(d, [True if i in comb else False for i in range(10)], 0, 0)
        if s > 0:
            ans += s
            break
        m -= 1