# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:11:11 2018

@author: lamwa
"""

import utils

SUP = 150000000

ans = 0
for n in range(10, SUP, 10):
    if n % 1000000 == 0:
        print(n)
    s = n * n
    if (s % 3 != 1): continue
    if (s % 7 != 2 and s % 7 != 3): continue
    if (s % 9 == 0 or s % 13 == 0 or s % 27 == 0): continue
    if (    utils.miller_rabin(s +  1) and \
            utils.miller_rabin(s +  3) and \
            utils.miller_rabin(s +  7) and \
            utils.miller_rabin(s +  9) and \
            utils.miller_rabin(s + 13) and \
        not utils.miller_rabin(s + 19) and \
        not utils.miller_rabin(s + 21) and \
            utils.miller_rabin(s + 27)): ans += n;
print(ans)