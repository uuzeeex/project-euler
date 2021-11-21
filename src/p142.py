# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:56:01 2018

@author: lamwa
"""

import utils

done = False
i = 4
while not done:
    a = i * i
    j = i - 1
    while not done and j > 0:
        c = j * j
        f = a - c
        if not utils.is_square(f):
            j -= 1
            continue
        k = j - 1
        while not done and k > 0:
            e = k * k
            d = a - e
            b = c - e
            if not utils.is_square(d) or not utils.is_square(b):
                k -= 1
                continue
            if (a + c + e) % 2 == 0:
                ans = (a + c + e) // 2
                done = True
            k -= 1
        j -= 1
    i += 1
print(ans)
