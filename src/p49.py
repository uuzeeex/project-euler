# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:22:28 2018

@author: lamwa
"""

import math

def is_per(n1, n2):
    return int(''.join(sorted(str(n1)))) == int(''.join(sorted(str(n2))))

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1000, 9998):
    for j in range(i + 1, 9999):
        k = j + j - i
        if k < 10000:
            if is_per(i, j) and is_per(j, k):
                if prime(i) and prime(j) and prime(k):
                    print(str(i) + str(j) + str(k))