# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:19:28 2018

@author: lamwa
"""

ans = 0

for a in range(101):
    for b in range(101):
        ans = max(ans, sum([int(c) for c in list(str(a ** b))]))

print(ans)