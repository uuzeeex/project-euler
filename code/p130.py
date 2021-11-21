# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:19:02 2018

@author: lamwa
"""

import utils

RANGE = 20000

def A(n):
    x = 1
    k = 1
    while x > 0:
        x = (x * 10 + 1) % n
        k += 1
    return k

is_p, _ = utils.sieve(RANGE)

ans = 0
n = 3
cnt = 0
while True:
    if not is_p[n]:
        if (n - 1) % A(n) == 0:
            ans += n
            cnt += 1
            if cnt == 25:
                break
    n += 2
    if n % 5 == 0:
        n += 2

print(ans)