# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:57:23 2018

@author: lamwa
"""

import urllib
import itertools

def check(s):
    sum_set = set()
    cur_max_len_level = 0
    for i in range(1, len(s) + 1):
        cur_max = 0
        for sub in itertools.combinations(s, i):
            cur_s = sum(sub)
            cur_max = max(cur_max, cur_s)
            if cur_s <= cur_max_len_level or cur_s in sum_set:
                return False
            sum_set.add(cur_s)
        cur_max_len_level = max(cur_max_len_level, cur_max)
    return True

with urllib.request.urlopen('https://projecteuler.net/project/resources/p105_sets.txt') as f:
    sets = [[int(s) for s in l.decode('utf-8').strip().split(',')] for l in f.readlines()]

print(sum(sum(s) for s in sets if check(s)))