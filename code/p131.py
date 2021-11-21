# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:01:45 2018

@author: lamwa
"""

import utils

SUP = 10 ** 6

ans = 0
a = 1
while True:
    p = (a + 1) ** 3 - a ** 3
    if p >= SUP:
        break
    if utils.miller_rabin(p):
        ans += 1
    a += 1
print(ans)