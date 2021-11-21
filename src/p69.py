# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:04:25 2018

@author: lamwa
"""

import utils

RANGE = 100
N = 1000000

_, p_list = utils.sieve(RANGE)

mul = 1
for p in p_list:
    mul *= p
    if mul > N:
        print(mul // p)
        break
