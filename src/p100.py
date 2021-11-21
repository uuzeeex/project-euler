# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 11:54:06 2018

@author: lamwa
"""

import math

RANGE = 1000000000000

a = [2, 14]

while True:
    new = a[-2] + 2 * round(math.sqrt(8 * a[-1] * a[-1] + 8 * a[-1] + 1))
    a.append(new)
    if (math.sqrt(8 * a[-1] * a[-1] + 8 * a[-1] + 1) - 1) // 2 > RANGE:
        print(a[-1] + 1)
        break