# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 18:15:50 2018

@author: lamwa
"""

def digit(n):
    res = 0
    while n > 0:
        n //= 10
        res += 1
    return res

F1 = 1
F2 = 1
cnt = 2
while True:
    F3 = F1 + F2
    cnt += 1
    if digit(F3) == 1000:
        print(cnt)
        break
    F1 = F2
    F2 = F3