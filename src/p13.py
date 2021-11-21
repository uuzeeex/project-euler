# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:16:21 2018

@author: lamwa
"""

with open('data13.txt') as f:
    l = [int(line) for line in f.readlines()]
ans = sum(l)