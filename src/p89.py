# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:09:28 2018

@author: lamwa
"""

import re

with open('p089_roman.txt') as f:
    file = f.read()

file_new = re.sub('IIII|VIIII|XXXX|LXXXX|CCCC|DCCCC', '**', file)
print(len(file) - len(file_new))