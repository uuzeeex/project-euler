# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:17:56 2018

@author: lamwa
"""

import utils

def find(n):
    if utils.is_square(n):
        return None
    s = utils.FracWithSqrt(0, 1, 1, n)
    a_i = list()
    while True:
        a_i.append(int(s.get_exact()))
        cur = utils.FracWithSqrt(a_i[-1], 0, 1, 0)
        for a in a_i[:: -1][1 :]:
            cur = cur.reciprocal().minus_int(-a)
        x, _, y = cur.get_val()
        if x * x - n * y * y == 1:
            return x
        rem = s.minus_int(a_i[-1])
        s = rem.reciprocal()
    return None

cur_max = 0
ans = 0
for i in range(2, 1001):
    cur = find(i)
    if cur is not None:
        if cur > cur_max:
            cur_max = cur
            ans = i
print(ans)