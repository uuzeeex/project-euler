# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:36:09 2018

@author: lamwa
"""

sum = 0

for i in range(1, 1001):
    sum += i ** i

print(sum % (10 ** 10))