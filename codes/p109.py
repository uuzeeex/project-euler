# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 21:47:24 2018

@author: lamwa
"""

import itertools

pts = [i for i in range(1, 21)] + [25]
times = [[1, 2, 3] for _ in range(20)] + [[1, 2]]

darts = [(pt, t) for pt, time in zip(pts, times) for t in time]

ans = 0
for dart_last in darts:
    if dart_last[1] == 2:
        cnt = 1
        for dart_1 in darts:
            if dart_1[0] * dart_1[1] + dart_last[0] * dart_last[1] < 100:
                cnt += 1
        for i, dart_1 in enumerate(darts):
            for dart_2 in darts[i :]:
                if dart_1[0] * dart_1[1] + dart_2[0] * dart_2[1] + dart_last[0] * dart_last[1] < 100:
                    cnt += 1
        ans += cnt

print(ans)