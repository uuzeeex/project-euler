# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:30:28 2018

@author: lamwa
"""

import utils
import itertools
import copy

RANGE = 1000000

is_p, _ = utils.sieve(RANGE)

def check(s, p, start):
    s_copy = copy.deepcopy(s)
    res = -1
    cnt = 0
    if is_p[int(''.join(s))]:
        if res == -1:
            res = int(''.join(s))
    else:
        cnt = 1
    for i in range(start, 10):
        for pos in p:
            s_copy[pos] = str(i)
        if is_p[int(''.join(s_copy))]:
            if res == -1:
                res = int(''.join(s_copy))
        else:
            cnt += 1
        if cnt > 2 - start + 1:
            return -1
    return res
            

def cal():
    for i in range(2, RANGE):
        s = list(str(i))
        if '0' in s:
            z_pos = [i for i, e in enumerate(s) if e == '0']
            c = list()
            for j in range(1, len(z_pos) + 1):
                c += list(itertools.combinations(z_pos, j))
            for p in c:
                ch = check(s, p, 1)
                if ch != -1:
                    return ch
        if s[0] == '1':
            z_pos = [i for i, e in enumerate(s) if e == '1']
            c = list()
            for j in range(1, len(z_pos) + 1):
                c += list(itertools.combinations(z_pos, j))
            for p in c:
                ch = check(s, p, 2)
                if ch != -1:
                    return ch
    return None

print(cal())