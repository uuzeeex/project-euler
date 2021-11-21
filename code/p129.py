# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:26:05 2018

@author: lamwa
"""

TH = 1000000

def A(n):
    x = 1
    k = 1
    while x > 0:
        x = (x * 10 + 1) % n
        k += 1
    return k

n = TH + 1
while A(n) <= TH:
    n += 2
    if n % 5 == 0:
        n += 2
print(n)