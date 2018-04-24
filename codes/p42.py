# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 14:23:11 2018

@author: lamwa
"""

import ast
import math

def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def is_tri(n):
    if is_square(1 + 8 * n):
        return (round(math.sqrt(1 + 8 * n)) - 1) % 2 == 0
    return False

def cal_val(word):
    val = 0
    for c in word:
        val += ord(c) - ord('A') + 1
    return val

with open('p042_words.txt') as f:
    words_list = list(ast.literal_eval(f.read()))

ans = 0

for word in words_list:
    if is_tri(cal_val(word)):
        ans += 1

print(ans)
