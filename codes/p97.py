# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 00:40:13 2018

@author: lamwa
"""

import utils

print((utils.power_mod(2, 7830457, 10000000000) * 28433 + 1) % 10000000000)