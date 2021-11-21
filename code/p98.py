# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:32:43 2018

@author: lamwa
"""

import ast
import utils

with open('p098_words.txt') as f:
    word_list = list(ast.literal_eval(f.read()))

pairs = list()
for i, w1 in enumerate(word_list[: -1]):
    for w2 in word_list[i + 1 :]:
        if sorted(w1) == sorted(w2):
            pairs.append((w1, w2))

RANGE = 1000000000
sqr_list = set()
i = 1
while i * i < RANGE:
    sqr_list.add(i * i)
    i += 1

ans = 0
for p in pairs:
    for s in sqr_list:
        if len(p[0]) == len(str(s)):
            c2d = dict()
            d2c = dict()
            match = True
            for c, d in zip(p[0], str(s)):
                if c not in c2d:
                    c2d[c] = d
                elif c2d[c] != d:
                    match = False
                    break
                if d not in d2c:
                    d2c[d] = c
                elif d2c[d] != c:
                    match = False
                    break
            if match:
                n2 = int(''.join([c2d[c] for c in p[1]]))
                if len(str(s)) == len(str(n2)) and utils.is_square(n2):
                    ans = max(ans, max(s, n2))

print(ans)
            