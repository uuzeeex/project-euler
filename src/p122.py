# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 23:34:10 2018

@author: lamwa
"""

N = 200

steps = [float('inf')] * (N + 1)

def dfs(n, path, depth):
    if n > N:
        return None
    steps[n] = min(steps[n], depth)
    if depth >= 11:
        return None
    dfs(n + n, path + [n], depth + 1)
    for m in path:
        dfs(n + m, path + [n], depth + 1)

dfs(1, [], 0)
ans = sum(steps[1 :])
print(ans)