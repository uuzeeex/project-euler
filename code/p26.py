# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 19:03:32 2018

@author: lamwa
"""

def cycle_len(d):
    cur_remain = 1
    cnt = 1
    remain_idx = dict()
    while True:
    	if cur_remain in remain_idx:
    		return cnt - remain_idx[cur_remain]
    	else:
    		remain_idx[cur_remain] = cnt
    	while cur_remain < d:
    		cur_remain *= 10
    	cur_remain %= d
    	if cur_remain == 0:
    		break
    	cnt += 1
    return 0

ans = 0
max_len = 0
for i in range(2, 1000):
	cur = cycle_len(i)
	if cur > max_len:
		max_len = cur
		ans = i

print(ans)