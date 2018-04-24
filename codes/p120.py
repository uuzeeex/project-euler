# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:16:11 2018

@author: lamwa
"""

ans = 0
for a in range(3, 1001):
    rems = set()
    i = 0
    while True:
        rem = ((a - 1) ** i + (a + 1) ** i) % (a * a)
        if rem > 2:
            if rem in rems:
                break
            rems.add(rem)
        i += 1
    ans += max(rems)
print(ans)