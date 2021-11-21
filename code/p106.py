# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:36:49 2018

@author: lamwa
"""

import itertools

def if_test(c1, c2):
    b1 = all(e1 < e2 for e1, e2 in zip(c1, c2))
    b2 = all(e1 > e2 for e1, e2 in zip(c1, c2))
    return b1 or b2

n = 12
l = [i for i in range(1, 13)]
ans = 0
for i in range(1, n // 2 + 1):
    cur = list(itertools.combinations(l, i))
    for pair in list(itertools.combinations(cur, 2)):
        if len(set(pair[0]) & set(pair[1])) == 0:
            if not if_test(*pair):
                ans += 1

print(ans)