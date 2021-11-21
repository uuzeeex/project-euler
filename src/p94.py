# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 17:06:55 2018

@author: lamwa
"""

import utils

RANGE = 1000000000

f1 = list()

for i in range(1, 1000):
    if utils.is_square((3 * i + 1) * (i + 1)):
        f1.append(i)

while True:
    new = 14 * f1[-1] - f1[-2] + 8
    if 6 * new + 2 <= RANGE:
        f1.append(new)
    else:
        break

f2 = list()

for i in range(2, 1000):
    if utils.is_square((3 * i - 1) * (i - 1)):
        f2.append(i)

while True:
    new = 15 * f2[-1] - 15 * f2[-2] + f2[-3]
    if 6 * new - 2 <= RANGE:
        f2.append(new)
    else:
        break

print(sum([6 * k + 2 for k in f1] + [6 * k - 2 for k in f2]))