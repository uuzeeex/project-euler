# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:39:29 2018

@author: lamwa
"""

SUP = 2000

import utils
import copy

def count(n, n_list):
    return sum(utils.miller_rabin(abs(n - e)) for e in n_list)

prev_v = [1, 1, 1, 1, 1, 1]
v = [2, 3, 4, 5, 6, 7]
dv = [6, 7, 8, 9, 10, 11]
ddv = 6

pd3 = [1]
l = 1
while len(pd3) < SUP:
    last = v[0] + dv[0] - 1
    next_last = v[0] + dv[0] + dv[0] + ddv - 1
    if count(v[0], [prev_v[0], last, v[0] + 1, next_last, v[0] + dv[0], v[0] + dv[0] + 1]) == 3:
        pd3.append(v[0])
    for e, prev_e, d in zip(v[1 :], prev_v[1 :], dv[1 :]):
        if count(e, [prev_e, e - 1, e + 1, e + d - 1, e + d, e + d + 1]) == 3:
            pd3.append(e)
    if l > 1 and count(last, [v[0], last - 1, v[0] - 1, prev_v[0], next_last, next_last - 1]) == 3:
        pd3.append(last)
    prev_v = copy.deepcopy(v)
    v = [e + de for e, de in zip(v, dv)]
    dv = [e + ddv for e in dv]
    l += 1

print(pd3[-1])