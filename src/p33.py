# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 07:51:28 2018

@author: lamwa
"""

import math

prod_n = 1
prod_d = 1

def cancel(n, d):
    if n % 10 == d // 10 and d % 10 > 0 and (n // 10) / (d % 10) == n / d:
        return True
    if n // 10 == d % 10 and (n % 10) / (d // 10) == n / d:
        return True
    return False

for n in range(10, 99):
    for d in range(n + 1, 100):
        if cancel(n, d):
            prod_n *= n
            prod_d *= d

print(prod_d // math.gcd(prod_n, prod_d))