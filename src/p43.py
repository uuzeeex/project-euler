# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:42:27 2018

@author: lamwa
"""

import itertools

per = list(itertools.permutations([str(i) for i in range(10)]))[362880 :]

p = [2, 3, 5, 7, 11, 13, 17]

ans = 0

def check(t):
    for i in range(1, 8):
        if int(''.join(t[i : i + 3])) % p[i - 1] != 0:
            return False
    return True

for t in per:
    if check(t):
        ans += int(''.join(t))

print(ans)