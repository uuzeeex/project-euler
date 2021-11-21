# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 12:05:49 2018

@author: lamwa
"""

import utils

RANGE = 100

C = utils.combination_number(RANGE, RANGE)

cnt = 0
for i in range(1, RANGE + 1):
    for j in range(1, i + 1):
        cnt += 1 if C[i, j] > 1e6 else 0

print(cnt)