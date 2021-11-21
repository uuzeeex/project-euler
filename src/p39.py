# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 15:05:58 2018

@author: lamwa
"""

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

cnt = [0] * 1001

for a in range(1, 1000):
    for b in range(1, 1000):
        if is_square(a * a + b * b):
            c = round(math.sqrt(a * a + b * b))
            if a + b + c <= 1000:
                cnt[a + b + c] += 1

import numpy as np
print(np.argmax(cnt))