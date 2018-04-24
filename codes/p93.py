# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 23:12:19 2018

@author: lamwa
"""

import itertools


def dfs(tup):
    l = len(tup)
    if l == 1:
        return [tup[0]]
    ret = set()
    for i in range(1, l):
        left = dfs(tup[: i])
        right = dfs(tup[i :])
        plus = set(l + r for l in left for r in right)
        minus = set(l - r for l in left for r in right)
        times = set(l * r for l in left for r in right)
        div = set(l / r for l in left for r in right if r != 0)
        ret |= plus | minus | times | div
    return ret

def cons(s):
    i = 1
    while i in s:
        i += 1
    return i - 1

cur_max = 0
global ans
combs = list(itertools.combinations([i for i in range(10)], 4))
for comb in combs:
    tars = set()
    for perm in list(itertools.permutations(comb)):
        tars |= dfs(perm)
    cur = cons(tars)
    if cur > cur_max:
        cur_max = cur
        ans = ''.join([str(d) for d in comb])

print(ans)