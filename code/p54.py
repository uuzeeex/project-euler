# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:04:30 2018

@author: lamwa
"""

hands = list()

def get_detail(hand):
    vals = [to_val(card[0]) for card in hand]
    suits = [card[1] for card in hand]
    vals, suits = (list(x) for x in zip(*sorted(zip(vals, suits), key=lambda pair: pair[0])))
    if vals == [10, 11, 12, 13, 14] and suits.count(suits[0]) == 5:
        return (10, vals[:: -1]), []
    if [v - vals[i] for i, v in enumerate(vals[1:])].count(1) == 4 and suits.count(suits[0]) == 5:
        return (9, vals[:: -1]), []
    if vals[: 4].count(vals[0]) == 4:
        return (8, vals[: 4]), [vals[4]]
    if vals[1 :].count(vals[1]) == 4:
        return (8, vals[1 :]), [vals[0]]
    if vals[: 3].count(vals[0]) == 3 and vals[3] == vals[4]:
        return (7, vals[: 3]), vals[3 :]
    if vals[2 :].count(vals[2]) == 3 and vals[0] == vals[1]:
        return (7, vals[2 :]), vals[: 2]
    if suits.count(suits[0]) == 5:
        return (6, vals[:: -1]), []
    if [v - vals[i] for i, v in enumerate(vals[1:])].count(1) == 4:
        return (5, vals[:: -1]), []
    if vals[: 3].count(vals[0]) == 3:
        return (4, vals[: 3]), [vals[4], vals[3]]
    if vals[1 : 4].count(vals[1]) == 3:
        return (4, vals[1 : 4]), [vals[4], vals[0]]
    if vals[2 :].count(vals[2]) == 3:
        return (4, vals[2 :]), [vals[1], vals[0]]
    if vals[0] == vals[1] and vals[2] == vals[3]:
        return (3, [vals[3], vals[2], vals[1], vals[0]]), [vals[4]]
    if vals[1] == vals[2] and vals[3] == vals[4]:
        return (3, [vals[4], vals[3], vals[2], vals[1]]), [vals[0]]
    if vals[0] == vals[1] and vals[3] == vals[4]:
        return (3, [vals[4], vals[3], vals[1], vals[0]]), [vals[2]]
    if vals[0] == vals[1]:
        return (2, [vals[1], vals[0]]), [vals[4], vals[3], vals[2]]
    if vals[1] == vals[2]:
        return (2, [vals[2], vals[1]]), [vals[4], vals[3], vals[0]]
    if vals[2] == vals[3]:
        return (2, [vals[3], vals[2]]), [vals[4], vals[1], vals[0]]
    if vals[3] == vals[4]:
        return (2, [vals[4], vals[3]]), [vals[2], vals[1], vals[0]]
    return (1, [vals[4]]), vals[: 4][:: -1]

def to_val(v):
    if v == 'T':
        return 10
    if v == 'J':
        return 11
    if v == 'Q':
        return 12
    if v == 'K':
        return 13
    if v == 'A':
        return 14
    return int(v)

def win(p1, p2):
    d1 = get_detail(p1)
    d2 = get_detail(p2)
    if d1[0][0] != d2[0][0]:
        return d1[0][0] > d2[0][0]
    h1 = d1[0][1] + d1[1]
    h2 = d2[0][1] + d2[1]
    for c1, c2 in zip(h1, h2):
        if c1 != c2:
            return c1 > c2
    return False

with open('p054_poker.txt') as f:
    for l in f.readlines():
        s = l.strip().split(' ')
        hands.append((s[: 5], s[5 :]))

ans = 0
for hand in hands:
    if win(hand[0], hand[1]):
        ans += 1
