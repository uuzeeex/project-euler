# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:11:20 2018

@author: lamwa
"""

SUP = 2 * (10 ** 4)

def f(l, a, b, c):
    return 2 * (a * b + b * c + c * a) + 4 * (l - 1) * (a + b + c + l - 2)

cnt = [0] * SUP

a = 1
while f(1, a, a, a) < SUP:
    b = a
    while f(1, a, b, b) < SUP:
        c = b
        while f(1, a, b, c) < SUP:
            l = 1
            while f(l, a, b, c) < SUP:
                cnt[f(l, a, b, c)] += 1
                l += 1
            c += 1
        b += 1
    a += 1

ans = 0
for i, c in enumerate(cnt):
    if c == 1000:
        ans = i
        break

print(ans)