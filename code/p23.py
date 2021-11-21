# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:55:39 2018

@author: lamwa
"""

import math
import numpy as np

def abundant(n):
    res = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if i * i == n:
            res += i
        elif n % i == 0:
            res += i + (n // i)
    return res > n

abundant_nums = []
for i in range(28123):
    if abundant(i + 1):
        abundant_nums.append(i + 1)

flag = np.zeros(28124, dtype=bool)

for a in abundant_nums:
    for b in abundant_nums:
        if a + b <= 28123:
            flag[a + b] = True

print(sum(np.where(flag == False)[0]))