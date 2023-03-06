# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 20:56:53 2018

@author: lamwa
"""

import utils

RANGE = 1000000


_, p_list = utils.sieve(RANGE)

s = list()
max_len = 0

for p in p_list:
    if s:
        if s[-1] + p < RANGE:
            max_len = len(s) + 1
        s.append(s[-1] + p)
    else:
        s.append(p)


def cal():
    for l in range(max_len, 0, -1):
        for i in range(len(s) - l + 1):
            cur = s[i + l - 1] - (s[i - 1] if i > 0 else 0)
            if cur < RANGE:
                if cur in p_list:
                    return cur
            else:
                break


print(cal())
