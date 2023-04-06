from timer import Timer

_MOD = 10 ** 6


class P710Solver:
    def solve(self):

        # ordered integer break counts without 2's
        f_0, f_1 = 1, 1
        s = 2
        # p[n] = 2^(n-1)
        p = [None, 1]
        # ordered integer break counts with 2's
        g = [0, 0]
        # answer but middle 2 doesn't count as 2
        h = 0

        n = 2
        while True:
            f_0, f_1 = f_1, (s - f_0) % _MOD
            s = (s + f_1) % _MOD
            p.append((p[-1] << 1) % _MOD)
            g.append((p[-1] - f_1) % _MOD)
            if n & 1 == 0:
                h = (h + g[n >> 1]) % _MOD
            t = h
            if n == 2:
                t = 1
            elif n & 1 == 0:
                m = n - 2 >> 1
                t = (t - g[m] + p[m]) % _MOD
            if n > 42 and t == 0:
                return n
            n += 1


if __name__ == '__main__':
    with Timer('P710'):
        p710_solver = P710Solver()
        print(p710_solver.solve())
