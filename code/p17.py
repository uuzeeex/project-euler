# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:21:01 2018

@author: lamwa
"""

digit = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [6, 6, 5, 5, 5, 7, 6, 6]
hun = 7

def char_count(n):
    if n == 0:
        return 0
    if n == 1000:
        return 11
    if n < 20:
        return digit[n - 1]
    elif n < 100:
        return tens[n // 10 - 2] + char_count(n % 10)
    elif n % 100 == 0:
        return digit[n // 100 - 1] + hun
    return digit[n // 100 - 1] + hun + 3 + char_count(n % 100)

ans = 0
for i in range(1, 1001):
    ans += char_count(i)

print(ans)