# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:54:44 2018

@author: lamwa
"""

def f(n):
    return sum((-n) ** i for i in range(11))

def pred(u):
    delta = [u]
    for i in range(len(u) - 1):
        delta.append([cur - prev for prev, cur in zip(delta[-1][: -1], delta[-1][1 :])])
    return sum(d[-1] for d in delta)
    
u = list()
ans = 0
for i in range(1, 11):
    u.append(f(i))
    ans += pred(u)

print(ans)