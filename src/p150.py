# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:50:51 2018

@author: lamwa
"""

N = 1000

import utils

s = utils.lgg(N * (N + 1) // 2)

tri = [s[i * (i - 1) // 2: i * (i - 1) // 2 + i] for i in range(1, N + 1)]

p_sum = [[0] for _ in range(N)]
for i in range(N):
    for e in tri[i]:
        p_sum[i].append(e + p_sum[i][-1])

ans = float('inf')
for i in range(N):
    for j in range(i + 1):
        cur = 0
        for k in range(N - i):
            cur += p_sum[i + k][j + k + 1] - p_sum[i + k][j]
            ans = min(ans, cur)
print(ans)
