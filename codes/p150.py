# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:50:51 2018

@author: lamwa
"""

N = 1000

import utils

s = utils.lgg(N * (N + 1) // 2)

tri = [s[i * (i - 1) // 2 : i * (i - 1) // 2 + i] for i in range(1, N + 1)]
