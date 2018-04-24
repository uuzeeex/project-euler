# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 23:38:18 2018

@author: lamwa
"""

import utils

def dfs(rem, s, prev):
    if len(rem) == 0 and s == 0:
        return 1
    cnt = 0
    for d in rem:
        next_s = s * 10 + d
        if next_s > prev and utils.miller_rabin(next_s):
            cnt += dfs(rem - set([d]), 0, next_s)
        cnt += dfs(rem - set([d]), next_s, prev)
    return cnt

ans = dfs(set([i for i in range(1, 10)]), 0, 0)
print(ans)