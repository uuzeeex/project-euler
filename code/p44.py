# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:16:15 2018

@author: lamwa
"""

import math

def p(n):
    return n * (3 * n - 1) // 2

def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def is_p(p):
    if is_square(1 + 24 * p):
        return (1 + round(math.sqrt(1 + 24 * p))) % 6 == 0
    return False

ans = float('inf')

for i in range(1, 3000):
    for j in range(i + 1, 3001):
        if is_p(p(i) + p(j)) and is_p(p(j) - p(i)):
            ans = min(ans, p(j) - p(i))

print(ans)