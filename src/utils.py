# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:31:11 2018

@author: lamwa
"""

import math
from collections import namedtuple
from fractions import Fraction
from typing import Iterator

import numpy as np
import random
import copy

Point = namedtuple('Point', 'x y')
Segment = namedtuple('Segment', 'p1 p2')
Vector = namedtuple('Vector', 'x y')

PointGridType = Point[int, int]
PointRationalType = Point[Fraction, Fraction]

SegmentGridType = Segment[Point[int, int], Point[int, int]]
VectorGridType = Vector[int, int]


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
            phi = phi * (p - 1) // p
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


def lgg(n):
    t, s = 0, []
    for k in range(1, n + 1):
        t = (615949 * t + 797807) % (1 << 20)
        s.append(t - (1 << 19))
    return s


def max_sub(a):
    f = [a[0]]
    for e in a[1:]:
        f.append(max(f[-1] + e, e))
    return max(f)


def arithmetic_seq_sum(first: int, delta: int, n: int) -> int:
    return (((first << 1) + (n - 1) * delta) * n) >> 1


def natural_num_sum(n: int) -> int:
    return (n * (n + 1)) >> 1


def natural_num_squ_sum(n: int) -> int:
    return (n * (n + 1) * (2 * n + 1)) // 6


def fibonacci_by_upper_bound(u: int) -> Iterator[int]:
    f = [1, 1]
    while f[0] <= u:
        yield f[0]
        f[1] += f[0]
        f[0] = f[1] - f[0]


def blum_blum_shub(n: int) -> Iterator[int]:
    s = 290797
    for i in range(n):
        s = s * s % 50515093
        yield s % 500


def vector(p1: PointGridType, p2: PointGridType) -> VectorGridType:
    return Vector(p2.x - p1.x, p2.y - p1.y)


def cross_prod(v1: VectorGridType, v2: VectorGridType) -> int:
    return v1.x * v2.y - v2.x * v1.y


def true_intersection(s1: SegmentGridType, s2: SegmentGridType) -> bool:
    v1, v2 = vector(s1.p1, s1.p2), vector(s2.p1, s2.p2)
    v11, v12 = vector(s1.p2, s2.p1), vector(s1.p2, s2.p2)
    v21, v22 = vector(s2.p2, s1.p1), vector(s2.p2, s1.p2)
    both_sides_1 = cross_prod(v1, v11) * cross_prod(v1, v12) < 0
    both_sides_2 = cross_prod(v2, v21) * cross_prod(v2, v22) < 0
    if both_sides_1 and both_sides_2:
        return True
    return False


def intersection(s1: SegmentGridType, s2: SegmentGridType) -> PointRationalType | None:
    dx1, dy1 = s1.p2.x - s1.p1.x, s1.p2.y - s1.p1.y
    dx2, dy2 = s2.p2.x - s2.p1.x, s2.p2.y - s2.p1.y
    if dx1 * dy2 == dx2 * dy1:
        return None
    x = Fraction(
        dx2 * (s1.p1.y * dx1 - s1.p1.x * dy1) - dx1 * (s2.p1.y * dx2 - s2.p1.x * dy2),
        dx1 * dy2 - dx2 * dy1
    )
    if dx1 != 0:
        y = (x - s1.p1.x) * dy1 / dx1 + s1.p1.y
    else:
        y = (x - s2.p1.x) * dy2 / dx2 + s2.p1.y
    return PointRationalType(x, y)
