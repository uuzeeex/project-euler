# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:09:31 2018

@author: lamwa
"""

import copy
import math

def num_pfac(n):
    n_copy = copy.deepcopy(n)
    num = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n_copy % i == 0:
            num += 1
            while n_copy % i == 0:
                n_copy //= i
    if n_copy > 1:
        num += 1
    return num

i = 2
while True:
    if num_pfac(i) == 4 and num_pfac(i + 1) == 4 and num_pfac(i + 2) == 4 and num_pfac(i + 3) == 4:
        print(i)
        break
    i += 1
