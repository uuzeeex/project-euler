# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:02:15 2018

@author: lamwa
"""

RANGE = 10000000

rec = dict()

def dfs(i, rec):
    if i in rec:
        return rec[i]
    if i == 1 or i == 89:
        res = i
    else:
        res = dfs(sum(int(c) * int(c) for c in str(i)), rec)
    rec[i] = res
    return res

ans = 0
for i in range(1, RANGE):
    ans += (dfs(i, rec) == 89)
print(ans)
