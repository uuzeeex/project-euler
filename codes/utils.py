# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:31:11 2018

@author: lamwa
"""

import math
import numpy as np
import random
import copy

def sieve(r):
    is_p = np.ones(r, dtype=bool)
    is_p[0] = False
    is_p[1] = False
    for i in range(2, r):
        for j in range(i, (r - 1) // i + 1):
            is_p[i * j] = False
    return is_p, [i for i in range(r) if is_p[i]]

def combination_number(n, r):
    C = np.zeros((n + 1, r + 1))
    C[:, 0] = 1
    for i in range(1, n + 1):
        for j in range(1, r + 1):
            C[i, j] = C[i - 1, j] + C[i - 1, j - 1]
    return C

def check_palindrome(n):
    return str(n)[::-1] == str(n)

def power_mod(a, b, c):
    if b == 0:
        return 1
    pm = power_mod((a * a) % c, b >> 1, c)
    if b & 1 == 0:
        return pm
    return (a * pm) % c

def miller_rabin(n, k=9):
    if n < 2:
        return False
    for t in range(k):
        a = random.randint(1, n - 1)
        n_copy = copy.deepcopy(n) - 1
        p = False
        while n_copy % 2 == 0:
            n_copy //= 2
            if power_mod(a, n_copy, n) == n - 1:
                p = True
                break
        sth_power = power_mod(a, n_copy, n)
        if (not p) and (sth_power == n - 1 or sth_power == 1):
            p = True
        if not p:
            return False
    return True 

def rad(n):
    ret, i = 1, 2
    while i * i <= n:
        if n % i == 0:
            ret *= i
            while n % i == 0:
                n //= i
        i += 1
    if n != 1:
        ret *= n
    return ret

def tri(n):
    return n * (n + 1) // 2

def squ(n):
    return n * n

def penta(n):
    return n * (3 * n - 1) // 2

def hexa(n):
    return n * (2 * n - 1)

def hepta(n):
    return n * (5 * n - 3) // 2

def octa(n):
    return n * (3 * n - 2)

def is_square(n):
    if n < 0: return False
    s = round(math.sqrt(n))
    return s * s == n

def is_triangle(t):
    if is_square(1 + 8 * t):
        return (-1 + round(math.sqrt(1 + 8 * t))) % 2 == 0
    return False

def is_pentagonal(p):
    if is_square(1 + 24 * p):
        return (1 + round(math.sqrt(1 + 24 * p))) % 6 == 0
    return False

def is_hexagonal(h):
    if is_square(1 + 8 * h):
        return (1 + round(math.sqrt(1 + 8 * h))) % 4 == 0
    return False

def is_heptagonal(h):
    if is_square(9 + 40 * h):
        return (3 + round(math.sqrt(9 + 40 * h))) % 10 == 0
    return False

def is_octagonal(o):
    if is_square(4 + 12 * o):
        return (2 + round(math.sqrt(4 + 12 * o))) % 6 == 0
    return False

class FracWithSqrt(object):
    def __init__(self, a=0, b=0, c=1, base=0):
        self.a = a
        self.b = b
        self.c = c
        self._to_pos()
        self._divide()
        self.base = base
    
    def _to_pos(self):
        if self.c < 0:
            self.a //= -1
            self.b //= -1
            self.c //= -1
        
    def _divide(self):
        divisor = self.c
        if self.a != 0:
            divisor = math.gcd(divisor, self.a)
        if self.b != 0:
            divisor = math.gcd(divisor, self.b)
        self.a //= divisor
        self.b //= divisor
        self.c //= divisor
        
    def reciprocal(self):
        ra = self.a * self.c
        rb = -self.b * self.c
        rc = self.a * self.a - self.b * self.b * self.base
        return FracWithSqrt(a=ra, b=rb, c=rc, base=self.base)
    
    def minus_int(self, n):
        ma = self.a - self.c * n
        return FracWithSqrt(a=ma, b=self.b, c=self.c, base=self.base)
    
    def get_exact(self):
        return (self.a + self.b * math.sqrt(self.base)) / self.c

    def get_val(self):
        return self.a, self.b, self.c

def phi(n, p_list):
    phi = copy.deepcopy(n)
    d = copy.deepcopy(n)
    for p in p_list:
        if d % p == 0:
            phi = phi * (p - 1) //  p
            while d % p == 0:
                d //= p
        if d == 1:
            break
    return phi

def lfg(n):
    s = []
    for k in range(1, n + 1):
        if k <= 55:
            s.append((100003 - 200003 * k + 300007 * (k ** 3)) % (10 ** 6) - 5 * (10 ** 5))
        else:
            s.append((s[-24] + s[-55] + 10 ** 6) % (10 ** 6) - 5 * (10 ** 5))
    return s

def max_sub(a):
    f = [a[0]]
    for e in a[1 :]:
        f.append(max(f[-1] + e, e))
    return max(f)