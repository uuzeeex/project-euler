# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:33:26 2018

@author: lamwa
"""

def bouncy(n):
    b1 = True
    b2 = True
    while n // 10 > 0:
        p = n % 10
        q = (n // 10) % 10
        b1 &= p >= q
        b2 &= p <= q
        n //= 10
    return not (b1 | b2)

cnt = 0
i = 1
while cnt * 100 != i * 99:
    i += 1
    if bouncy(i):
        cnt += 1

print(i)