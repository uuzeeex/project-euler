# -*- coding: utf-8 -*-
"""
Created on Wed July 11 20:10:48 2018

@author: lamwa
"""

import fractions

N = 18

S = [set() for _ in range(N)]
S[0].add(fractions.Fraction(1, 1))

for k in range(1, N):
	for i in range(1, (k + 1) // 2 + 1):
		S[k] |= set(e1 + e2 for e1 in S[i - 1] for e2 in S[k - i])
		S[k] |= set(1 / (1 / e1 + 1 / e2) for e1 in S[i - 1] for e2 in S[k - i])

ans = len(set.union(*S))
print(ans)