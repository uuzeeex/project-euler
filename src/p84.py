# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:54:35 2018

@author: lamwa
"""

import random
import numpy as np

TIMES = 100
STEPS = 10000

cc = [1, 2] + [0] * 14
ch = [i for i in range(1, 11)] + [0] * 6
rails = [5, 15, 25, 35]

def move_cc(pos, card):
    if card == 1:
        return 0
    if card == 2:
        return 10
    return pos

def move_ch(pos, card):
    if card == 1:
        return 0
    if card == 2:
        return 10
    if card == 3:
        return 11
    if card == 4:
        return 24
    if card == 5:
        return 39
    if card == 6:
        return 5
    if card == 7 or card == 8:
        for r in rails:
            if r > pos:
                return r
        return rails[0]
    if card == 9:
        if 12 > pos:
            return 12
        if 28 > pos:
            return 28
        return 12
    if card == 10:
        return (pos - 3) % 40
    return pos

cnt = [0] * 40

for T in range(TIMES):
    random.shuffle(cc)
    random.shuffle(ch)
    consec = 0
    cur_pos = 0
    cc_pnt = 0
    ch_pnt = 0
    for s in range(STEPS):
        dice1 = random.randint(1, 4)
        dice2 = random.randint(1, 4)
        if dice1 == dice2:
            consec += 1
        else:
            consec = 0
        s = dice1 + dice2
        cur_pos = (cur_pos + s) % 40
        if consec == 3 or cur_pos == 30:
            consec = 0
            cur_pos = 10
            cnt[cur_pos] += 1
            continue
        if cur_pos in set([2, 17, 33]):
            cur_pos = move_cc(cur_pos, cc[cc_pnt])
            cc_pnt = (cc_pnt + 1) % 16
        if cur_pos in set([7, 22, 36]):
            cur_pos = move_ch(cur_pos, ch[ch_pnt])
            ch_pnt = (ch_pnt + 1) % 16
        cnt[cur_pos] += 1

ans = ''
for pos in np.argsort(cnt)[:: -1][: 3]:
    if pos < 10:
        ans += '0' + str(pos)
    else:
        ans += str(pos)
print(ans)