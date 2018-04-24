# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:12:22 2018

@author: lamwa
"""

cnt = dict()
nums = dict()

for i in range(1, 10000):
    cube = i * i * i
    key = ''.join(sorted(str(cube)))
    if key not in cnt:
        cnt[key] = 1
        nums[key] = [cube]
    else:
        cnt[key] += 1
        nums[key].append(cube)

for key, times in cnt.items():
    if times == 5:
        print(nums[key])