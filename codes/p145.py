# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:25:10 2018

@author: lamwa
"""

def cal(n):
    if (n - 1) % 4 == 0:
        return 0
    if n % 2 == 0:
        return 20 * (30 ** (n // 2 - 1))
    return 20 * ((25 * 20) ** (n // 4)) * 5

ans = 0
for i in range(1, 10):
    ans += cal(i)
print(ans)