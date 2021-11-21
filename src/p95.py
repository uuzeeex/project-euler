# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 23:57:51 2018

@author: lamwa
"""

RANGE = 1000000

s = [0] * (RANGE + 1)

for i in range(1, RANGE + 1):
    for j in range(2, RANGE // i + 1):
        s[i * j] += i

flag = [False] * (RANGE + 1)
cur_max = 0
h = 0
for i in range(RANGE + 1):
    if not flag[i]:
        cur_set = dict()
        p = i
        step = 0
        while p <= RANGE and (p not in cur_set):
            cur_set[p] = step
            flag[p] = True
            p = s[p]
            step += 1
        if p <= RANGE and step - cur_set[p] > cur_max:
            cur_max = step - cur_set[p]
            h = p

ans = h
p = s[h]
while p != h:
    ans = min(ans, h)
    p = s[p]