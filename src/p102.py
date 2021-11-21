# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:39:46 2018

@author: lamwa
"""

import urllib

with urllib.request.urlopen('https://projecteuler.net/project/resources/p102_triangles.txt') as f:
    triangles = [[int(s) for s in l.decode('utf-8').strip().split(',')] for l in f.readlines()]
    triangles = [[(x, y) for x, y in zip(t[:: 2], t[1 :: 2])] for t in triangles]

def cross(v1, v2):
    return v1[0] * v2[1] - v2[0] * v1[1]

def contain_origin(tri):
    v0 = (tri[1][0] - tri[0][0], tri[1][1] - tri[0][1])
    v1 = (tri[2][0] - tri[1][0], tri[2][1] - tri[1][1])
    v2 = (tri[0][0] - tri[2][0], tri[0][1] - tri[2][1])
    c0 = cross(v0, (-tri[0][0], -tri[0][1]))
    c1 = cross(v1, (-tri[1][0], -tri[1][1]))
    c2 = cross(v2, (-tri[2][0], -tri[2][1]))
    return (c0 > 0 and c1 > 0 and c2 > 0) or (c0 < 0 and c1 < 0 and c2 < 0)

ans = 0
for tri in triangles:
    if contain_origin(tri):
        ans += 1
print(ans)