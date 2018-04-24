# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 23:31:36 2018

@author: lamwa
"""

flag = [False] * 10
cur = [0] * 9
ans = ''

def argmax(pairs):
    return min(pairs, key=lambda x: x[1])[0]

def to_string(cur):
    t = [(10, cur[0], cur[1]), (cur[5], cur[1], cur[2]), (cur[6], cur[2], cur[3]), \
         (cur[7], cur[3], cur[4]), (cur[8], cur[4], cur[0])]
    pos = argmax(enumerate(t))
    t = t[pos :] + t[: pos]
    return ''.join([''.join([str(num) for num in tup]) for tup in t])

def dfs(depth):
    global ans
    if depth == 9:
        s1 = 10 + cur[0] + cur[1]
        s2 = cur[5] + cur[1] + cur[2]
        s3 = cur[6] + cur[2] + cur[3]
        s4 = cur[7] + cur[3] + cur[4]
        s5 = cur[8] + cur[4] + cur[0]
        if s1 == s2 and s2 == s3 and s3 == s4 and s4 == s5:
            ans = max(ans, to_string(cur))
    for i in range(1, 10):
        if not flag[i]:
            cur[depth] = i
            flag[i] = True
            dfs(depth + 1)
            flag[i] = False

dfs(0)
print(ans)