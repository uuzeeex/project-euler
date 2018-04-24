# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 23:33:44 2018

@author: lamwa
"""

RANGE = 30000

import utils
import math

def numcat(a,b):
    return int(math.pow(10, (int(math.log(b, 10)) + 1)) * a + b)

def check(p, q):
    return utils.miller_rabin(numcat(p, q)) and utils.miller_rabin(numcat(q, p))

_, p_list = utils.sieve(RANGE)
s = list()
for i, p in enumerate(p_list):
    s.append(list())
    for j, q in enumerate(p_list[i + 1 :]):
        if check(p, q):
            s[-1].append(j + i + 1)

def dfs(depth, cur, itsc):
    if depth == 5:
        print(cur)
        print(sum(cur))
        return None
    for i in itsc:
        dfs(depth + 1, cur + [p_list[i]], set(itsc).intersection(s[i]))
    return None
   
for i in range(len(s) - 4):
    dfs(1, [p_list[i]], s[i])