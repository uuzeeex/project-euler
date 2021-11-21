# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:40:01 2018

@author: lamwa
"""

import ast

def score(pos, name):
    val = 0
    for c in name:
        val += ord(c) - ord('A') + 1
    return pos * val

with open('p022_names.txt') as f:
    name_list = list(ast.literal_eval(f.read()))

name_list.sort()

ans = 0
for idx, name in enumerate(name_list):
    ans += score(idx + 1, name)

print(ans)