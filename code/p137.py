# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:56:51 2018

@author: lamwa
"""

N = 15

F = [0, 1]

for i in range(2, 2 * N + 2):
    F.append(F[-1] + F[-2])

print(F[2 * N] * F[2 * N + 1])