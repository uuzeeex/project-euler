# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:41:34 2018

@author: lamwa
"""

import fractions

HALF = fractions.Fraction(1, 2)
n_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 18, 20, 21, 24, \
          28, 30, 35, 36, 39, 40, 42, 45, 52, 56, 60, 63, 70, 72]
d = dict()
ans = 0
 
def dfs1(l, r, s):
    if l > r:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
        return
    dfs1(l + 1, r, s)
    dfs1(l + 1, r, s + fractions.Fraction(1, n_list[l] ** 2))

def dfs2(l, r, s):
    global ans
    if l > r:
        rem = HALF - s
        if rem in d:
            ans += d[rem]
        return
    dfs2(l + 1, r, s)
    dfs2(l + 1, r, s + fractions.Fraction(1, n_list[l] ** 2))

n = len(n_list)
dfs1(0, n // 2, fractions.Fraction(0))
dfs2(n // 2 + 1, n - 1, fractions.Fraction(0))
print(ans)