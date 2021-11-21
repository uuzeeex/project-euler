# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:47:17 2018

@author: lamwa
"""

import math

def cal_k(p):
    return -4 * p[0] / p[1]

def next_k(k1, k):
    return (k1 - k * k * k1 - 2 * k) / (k * k - 2 * k * k1 - 1)

def solve(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0: return None
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

def next_p(p0, k):
    x0, y0 = p0
    a = k * k + 4
    b = 2 * k * y0 - 2 * k * k * x0
    c = k * k * x0 * x0 + y0 * y0 - 2 * k * x0 * y0 - 100
    x1, x2 = solve(a, b, c)
    x = x1 if math.fabs(x0 - x1) > math.fabs(x0 - x2) else x2
    y = k * (x - x0) + y0
    return x, y

ans = 1
x, y = 1.4, -9.6
k = (y - 10.1) / (x - 0.)
while True:
    k = next_k(k, cal_k((x, y)))
    x, y = next_p((x, y), k)
    if math.fabs(x) <= 1e-2 and y > 0:
        break
    ans += 1
print(ans)