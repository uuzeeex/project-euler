# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:59:39 2018

@author: lamwa
"""

import utils

SUP = 10 ** 12

def f(a, x, y):
    return a * a * x * x * x * y + a * y * y

ans_set = set()
x = 2
while f(1, x, 1) < SUP:
    y = 1
    while y < x and f(1, x, y) < SUP:
        a = 1
        while f(a, x, y) < SUP:
            ns = f(a, x, y)
            if utils.is_square(ns):
                ans_set.add(ns)
ans = sum(ans_set)
print(ans)