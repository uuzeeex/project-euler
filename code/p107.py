# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:08:50 2018

@author: lamwa
"""

import urllib

edge_list = []
n = 0
with urllib.request.urlopen('https://projecteuler.net/project/resources/p107_network.txt') as f:
    for i, l in enumerate(f.readlines()):
        for j, s in enumerate(l.decode('utf-8').strip().split(',')):
            if i < j and s.isdigit():
                edge_list.append((i + 1, j + 1, int(s)))
                n = max(n, i + 1, j + 1)

edge_list = sorted(edge_list, key=lambda tup: tup[2])

f = [i for i in range(n + 1)]

def find(i):
    if f[i] != i:
        f[i] = find(f[i])
    return f[i]

mst = 0
cnt = 0
for e in edge_list:
    if find(e[0]) != find(e[1]):
        f[f[e[0]]] = f[e[1]]
        mst += e[2]
        cnt += 1
        if cnt == n - 1:
            break

print(sum(e[2] for e in edge_list) - mst)