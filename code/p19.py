# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:13:13 2018

@author: lamwa
"""

import datetime

start_date = datetime.date(1901, 1, 1)
end_date = datetime.date(2000, 12, 31)

delta = end_date - start_date

cnt = 0

for i in range(delta.days + 1):
    cur_date = start_date + datetime.timedelta(days=i)
    if cur_date.day == 1 and cur_date.weekday() == 6:
        cnt += 1

print(cnt)