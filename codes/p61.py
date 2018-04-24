# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:57:36 2018

@author: lamwa
"""

import utils
import networkx as nx

RANGE = 200

def num_type(n):
    types = list()
    if utils.is_triangle(n):
        types.append('A')
    if utils.is_square(n):
        types.append('B')
    if utils.is_pentagonal(n):
        types.append('C')
    if utils.is_hexagonal(n):
        types.append('D')
    if utils.is_heptagonal(n):
        types.append('E')
    if utils.is_octagonal(n):
        types.append('F')
    return types

def check(types):
    B = nx.Graph()
    B.add_nodes_from([i for i in range(len(types))], bipartite=0)
    B.add_nodes_from([chr(i + 65) for i in range(6)], bipartite=1)
    edges = list()
    for i, t in enumerate(types):
        edges += [(i, e) for e in t]
    B.add_edges_from(edges)
    return len(nx.bipartite.maximum_matching(B)) // 2 == len(types)

def dfs(depth, types, first, prev, s, nums):
    if len(types) == 6:
        if prev % 100 == first // 100:
            print(s)
            print(nums)
            return None
    if depth == 0:
        for i in range(1000, 10000):
            if (i // 10) % 10 == 0:
                continue
            cur_t = num_type(i)
            if cur_t:
                dfs(depth + 1, types + [cur_t], i, i, s + i, nums + [i])
    else:
        for i in range(11, 100):
            if (i // 10) % 10 == 0:
                continue
            cur_num = (prev % 100) * 100 + i
            cur_t = num_type(cur_num)
            if cur_t and check(types + [cur_t]):
                dfs(depth + 1, types + [cur_t], first, cur_num, s + cur_num, nums + [cur_num])
    return None

dfs(0, [], 0, 0, 0, [])