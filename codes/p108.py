# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 23:47:36 2018

@author: lamwa
"""

import math

SUP = 1000

def num_sol(n):
    ret = 1
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            ret *= 2 * cnt + 1
    if n > 1:
        ret *= 3
    return (ret + 1) // 2

n = 2
while num_sol(n) <= SUP:
    n += 1
print(n)