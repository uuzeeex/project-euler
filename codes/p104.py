# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 12:10:55 2018

@author: lamwa
"""

import math

def pand(s):
    return len(set(s) - set('0')) == 9

phi = (1 + math.sqrt(5)) / 2
f1 = 1
f2 = 1
n = 2
while True:
    n += 1
    f2 = (f1 + f2) % (10 ** 9)
    f1 = f2 - f1
    s = str(f2)
    p = n * math.log10(phi) - math.log10(math.sqrt(5))
    first = str(int(10 ** (p - int(p) + 8)))
    if pand(s) and pand(first):
        print(n)
        break