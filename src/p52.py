# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:56:52 2018

@author: lamwa
"""

def check(n1, n2):
    return ''.join(sorted(str(n1))) == ''.join(sorted(str(n2)))

i = 0
while True:
    i += 1
    flag = True
    for t in range(2, 7):
        if not check(i * (t - 1), i * t):
            flag = False
            break
    if flag:
        print(i)
        break