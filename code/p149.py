# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:07:52 2018

@author: lamwa
"""

import utils

N = 2000

s = utils.lfg(N * N)
s = [s[i : i + N] for i in range(0, len(s), N)]

row = max(utils.max_sub(r) for r in s)
col = max(utils.max_sub([r[j] for r in s]) for j in range(N))
diag_1 = max(utils.max_sub([s[i][k - i] for i in range(N) if k - i < N]) for k in range(2 * N - 1))
diag_2 = max(utils.max_sub([s[i][i - k] for i in range(N) if i - k < N]) for k in range(1 - N, N))

ans = max(row, col, diag_1, diag_2)
print(ans)