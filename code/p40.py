# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 15:15:35 2018

@author: lamwa
"""

def cal():
    pos = 1
    cnt = 0
    cur = 0
    ans = 1
    while True:
        cnt += 1
        for c in str(cnt):
            cur += 1
            d = int(c)
            if cur == pos:
                ans *= d
                if (pos == 1000000):
                    return ans
                pos *= 10
    return ans

print(cal())