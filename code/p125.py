# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:43:22 2018

@author: lamwa
"""

import utils

N = 10000
SUP = 100000000

s = [0]

for i in range(1, N + 1):
    s.append(s[-1] + i * i)

ans_set = set()
for i in range(1, N):
    for j in range(i + 1, N + 1):
        cur_s = s[j] - s[i - 1]
        if cur_s >= SUP:
            break
        if utils.check_palindrome(cur_s):
            ans_set.add(cur_s)
print(sum(ans_set))