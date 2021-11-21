# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:42:55 2018

@author: lamwa
"""

import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

i = 0
while True:
    i += 1
    cur = i * 2 + 1
    if prime(cur):
        continue
    ok = False
    for j in range(1, int(math.sqrt(cur / 2)) + 1):
        if prime(cur - 2 * j * j):
            ok = True
            break
    if not ok:
        print(cur)
        break

    