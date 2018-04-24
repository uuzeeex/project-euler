# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:37:41 2018

@author: lamwa
"""

ans = 0

def pan(n):
    cnt = 0
    flag = [False] * 9
    dnum = 0
    ret = 0
    while dnum < 9:
        cnt += 1
        cur = n * cnt
        for d in str(cur):
            dnum += 1
            if int(d) == 0 or flag[int(d) - 1]:
                return -1
            flag[int(d) - 1] = True
            ret = ret * 10 + int(d)
    return ret
    

for i in range(9999):
    ans = max(ans, pan(i + 1))

print(ans)