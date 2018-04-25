# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:11:11 2018

@author: lamwa
"""

import utils

SUP = 150000000
rems = [1, 3, 7, 9, 13, 27]

ans = 0
for n in range(10, SUP, 10):
    if n % 10000 == 0:
        print(n)
    s = n * n
    if all(utils.miller_rabin(s + rem) for rem in rems):
        ans += n
print(ans)