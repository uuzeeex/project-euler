# -*- coding: utf-8 -*-
"""
Created on Tue Sept 18 11:30:50 2018

@author: lamwa
"""

import math

def nCr(n, r):
	f = math.factorial
	return f(n) // f(r) // f(n - r)

ans = max(nCr(26, k) * (2 ** k - k - 1) for k in range(1, 27))

print(ans)