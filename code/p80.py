# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 00:26:01 2018

@author: lamwa
"""

from decimal import getcontext, Decimal
import utils

RANGE = 100

getcontext().prec = 105

ans = 0

for n in range(2, RANGE):
    if utils.is_square(n):
        continue
    sqrt = str(Decimal(n) ** Decimal('0.5'))
    sqrt = sqrt.replace('.', '')
    ans += sum(int(c) for c in sqrt[ : 100])

print(ans)