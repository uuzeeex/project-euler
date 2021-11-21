# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 23:38:08 2018

@author: lamwa
"""

RANGE = 12000

ans_max = RANGE * 2
ans = [ans_max] * (RANGE + 1)

def dfs(p, s, c, st):
    k = p - s + c
    if k <= RANGE:
        ans[k] = min(ans[k], p)
        for i in range(st, ans_max // p + 1):
            dfs(p * i, s + i, c + 1, i)

dfs(1, 1, 1, 2)

print(sum(set(ans[2 :])))