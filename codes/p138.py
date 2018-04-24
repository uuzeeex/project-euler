# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:54:20 2018

@author: lamwa
"""

import utils
import math

a = [8, 136, 2448]

for i in range(4, 13):
    a.append(17 * a[-1] + 17 * a[-2] - a[-3])

ans = 0
for k in a:
    h1 = 2 * k - 1
    h2 = 2 * k + 1
    if utils.is_square(k ** 2 + h1 ** 2):
        ans += round(math.sqrt(k ** 2 + h1 ** 2))
    else:
        ans += round(math.sqrt(k ** 2 + h2 ** 2))

print(ans)