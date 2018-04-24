# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 11:26:43 2018

@author: lamwa
"""

import utils

RANGE = 100
TH = 4000000

_, p_list = utils.sieve(RANGE)

ans = 1e20

def dfs(n, i, cur, r):
    global ans
    if n >= ans:
        return None
    if (cur + 1) // 2 > TH:
        ans = n
        return None
    for t in range(1, r + 1):
        n *= p_list[i]
        dfs(n, i + 1, cur * (2 * t + 1), t)

dfs(1, 0, 1, 100)