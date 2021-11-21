# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:21:01 2018

@author: lamwa
"""

import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def tr_prime(n):
    if not prime(n):
        return False
    s = str(n)
    l = len(s)
    for i in range(l - 1):
        if not prime(int(s[i + 1 :])):
            return False
    for i in range(l - 1):
        if not prime(int(s[: i + 1])):
            return False
    return True

ans = 0
cnt = 0
cur = 8
while cnt < 11:
    if tr_prime(cur):
        cnt += 1
        print(cur)
        ans += cur
    cur += 1

print(ans)