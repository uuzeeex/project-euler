# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:34:15 2018

@author: lamwa
"""

import math
import utils

def cal_len(n):
    if utils.is_square(n):
        return 0
    h = dict()
    cnt = 0
    s = utils.FracWithSqrt(0, 1, 1, n)
    while True:
        cnt += 1
        rem = s.minus_int(int(s.get_exact()))
        if rem.get_val() not in h:
            h[rem.get_val()] = cnt
        else:
            return cnt - h[rem.get_val()]
        s = rem.reciprocal()
    return None

ans = 0
for i in range(2, 10000):
    if cal_len(i) % 2 == 1:
        ans += 1

print(ans)