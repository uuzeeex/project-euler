# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 08:22:40 2018

@author: lamwa
"""

import math
import copy

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def cir_prime(n):
    n_cp = copy.deepcopy(n)
    base = 10 ** (len(str(n_cp)) - 1)
    for i in range(len(str(n_cp))):
        if not prime(n_cp):
            return False
        f = n_cp // base
        n_cp -= f * base
        n_cp = n_cp * 10 + f
    return True

cnt = 0
for i in range(2, 1000000):
    if cir_prime(i):
        cnt += 1

print(cnt)