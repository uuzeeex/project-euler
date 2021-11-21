# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 08:40:57 2018

@author: lamwa
"""

def check(n):
    ten = str(n)
    len_ten = len(ten)
    two = "{0:b}".format(n)
    len_two = len(two)
    for i in range(len_ten // 2):
        if ten[i] != ten[len_ten - i - 1]:
            return False
    for i in range(len_two // 2):
        if two[i] != two[len_two - i - 1]:
            return False
    return True


ans = 0
for i in range(1, 1000000):
    if check(i):
        ans += i
print(ans)