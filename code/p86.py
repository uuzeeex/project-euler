# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:07:27 2018

@author: lamwa
"""

import utils

n = 3
cnt = 0

while True:
    for k in range(2, n * 2 + 1):
        if utils.is_square(k * k + n * n):
            l = max(k - n, 1)
            r = k // 2
            cnt += r - l + 1
            #print(r - l + 1)
    if cnt > 1000000:
        print(n)
        break
    n += 1
