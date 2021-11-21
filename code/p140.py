# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:51:21 2018

@author: lamwa
"""

x = [7, 8, 13, 17]
m = [2]

while len(m) < 30:
    x.append(3 * x[-2] - x[-4])
    if (x[-1] - 7) % 5 == 0:
        m.append((x[-1] - 7) // 5)

ans = sum(m)
print(ans)