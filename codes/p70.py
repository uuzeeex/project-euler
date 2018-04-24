# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 03:33:04 2018

@author: lamwa
"""

import utils

RANGE = 5000

_, p_list = utils.sieve(RANGE)

cur_min = float('inf')
ans = 0

for p1 in p_list:
    for p2 in p_list:
        if p1 != p2:
            if ''.join(sorted(str(p1 * p2))) == ''.join(sorted(str((p1 - 1) * (p2 - 1)))):
                cur = p1 * p2 / ((p1 - 1) * (p2 - 1))
                if p1 * p2 < 1e7 and cur < cur_min:
                    cur_min = cur
                    ans = p1 * p2

print(ans)