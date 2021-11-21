# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:35:00 2018

@author: lamwa
"""

def decrypt(cipher, key):
    len_key = len(key)
    key_ascii = [ord(c) for c in key]
    plain = list()
    for i, c in enumerate(cipher):
        plain.append(c ^ key_ascii[i % len_key])
    return ''.join([chr(c) for c in plain])

with open('p059_cipher.txt') as f:
    cipher = [int(s) for s in f.read().strip().split(',')]

max_s_num = 0
for c1 in range(ord('a'), ord('z') + 1):
    for c2 in range(ord('a'), ord('z') + 1):
        for c3 in range(ord('a'), ord('z') + 1):
            cur_d = decrypt(cipher, chr(c1) + chr(c2) + chr(c3))
            s_num = sum([1 for c in cur_d if c == ' '])
            if s_num > max_s_num:
                max_s_num = s_num
                d = cur_d

print(sum([ord(c) for c in d]))