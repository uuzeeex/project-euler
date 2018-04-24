# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 17:53:39 2018

@author: lamwa
"""

import utils

RANGE = 1000000

_, p_list = utils.sieve(RANGE + 10)
p_list = p_list[2 :]

mul_table = {
    1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    3: [0, 7, 4, 1, 8, 5, 2, 9, 6, 3],
    7: [0, 3, 6, 9, 2, 5, 8, 1, 4, 7],
    9: [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
}

def find(a, b):
    ret = 0
    u = b % 10
    shift = 1
    while a > 0:
         ret += b * mul_table[u][(a - ret // shift) % 10] * shift
         a //= 10
         shift *= 10
    return ret

ans = 0
for i in range(1, len(p_list)):
    ans += find(p_list[i - 1], p_list[i])
print(ans)