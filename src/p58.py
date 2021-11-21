# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:57:20 2018

@author: lamwa
"""

import utils

cur = 0
cnt = 1
n = 1

while True:
    if utils.miller_rabin(4 * n * n - 2 * n + 1):
        cur += 1
    if utils.miller_rabin(4 * n * n + 1):
        cur += 1
    if utils.miller_rabin(4 * n * n + 2 * n + 1):
        cur += 1
    if utils.miller_rabin(4 * n * n + 4 * n + 1):
        cur += 1
    cnt += 4
    if cur / cnt < 0.1:
        print(n * 2 + 1)
        break
    n += 1