# -*- coding: utf-8 -*-
"""
Created on Sat May  5 21:44:32 2018

@author: lamwa
"""

mem = dict()
mem[(0, 0, 0, 1)] = 0.

def pick(cur, idx):
    return cur[: idx] + (cur[idx] - 1, ) + tuple(e + 1 for e in cur[idx + 1 :])

def dfs(cur):
    if cur in mem:
        return mem[cur]
    num = sum(cur)
    ret = 1. if num == 1 else 0.
    for i, rem in enumerate(cur):
        if rem > 0:
            ret += (rem / num) * dfs(pick(cur, i))
    if cur not in mem:
        mem[cur] = ret
    return ret

ans = dfs((1, 1, 1, 1))
print(round(ans, 6))