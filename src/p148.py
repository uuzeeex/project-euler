# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:57:33 2018

@author: lamwa
"""

RANGE = 10 ** 9

def a(i):
    if i == 0: return 1
    return a(i // 7) * (i % 7 + 1)

def S(i):
    if i == 0: return 0
    return S(i // 7) * 28 + sum(a(i - k - 1) for k in range(i % 7))

print(S(RANGE))