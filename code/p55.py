# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:04:51 2018

@author: lamwa
"""

import utils
import copy

RANGE = 10000

def lychrel(n):
    n_copy = copy.deepcopy(n)
    for i in range(50):
        n_copy = int(str(n_copy)[::-1]) + n_copy
        if utils.check_palindrome(n_copy):
            return False
    return True

cnt = 0
for i in range(1, RANGE):
    cnt += 1 if lychrel(i) else 0

print(cnt)