# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:41:19 2018

@author: lamwa
"""

import itertools

base = [20, 31, 38, 39, 40, 42, 45]

def check(s):
    sum_set = set()
    for i in range(1, len(s) + 1):
        for sub in itertools.combinations(s, i):
            cur_s = sum(sub)
            if cur_s in sum_set:
                return False
            else:
                sum_set.add(cur_s)
    return True

cur_min = float('inf')
ans = list()

def dfs(l, pos):
    global cur_min, ans
    if pos == len(l):
        if check(l) and sum(l) < cur_min:
            cur_min = sum(l)
            ans = l
        return None
    for d in range(-2, 3):
        l[pos] += d
        dfs(l, pos + 1)
        l[pos] -= d
    return None

dfs(base, 0)
print(''.join([str(e) for e in sorted(ans)]))