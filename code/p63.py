# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:24:34 2018

@author: lamwa
"""

cnt = 0

for i in range(1, 2000):
    base = 1
    while len(str(base ** i)) <= i:
        if len(str(base ** i)) == i:
            cnt += 1
        base += 1

print(cnt)