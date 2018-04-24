# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:55:47 2018

@author: lamwa
"""

import utils

RANGE = 1000000

_, p = utils.sieve(RANGE)

n = 1
while True:
    mod = p[n - 1] * p[n - 1]
    rem = (utils.power_mod(p[n - 1] - 1, n, mod) + utils.power_mod(p[n - 1] + 1, n, mod)) % mod
    if rem >= 10 ** 10:
        break
    n += 1

print(n)