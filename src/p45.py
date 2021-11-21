# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:35:42 2018

@author: lamwa
"""

import math

def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def t(n):
    return n * (n + 1) // 2

def is_p(p):
    if is_square(1 + 24 * p):
        return (1 + round(math.sqrt(1 + 24 * p))) % 6 == 0
    return False

def is_h(h):
    if is_square(1 + 8 * h):
        return (1 + round(math.sqrt(1 + 8 * h))) % 4 == 0
    return False

i = 285
while True:
    i += 1
    if is_p(t(i)) and is_h(t(i)):
        print(t(i))
        break