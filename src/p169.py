from timer import Timer


class P169Solver:
    def solve(self, n: int = 10 ** 25):
        # f_0 - break the current 1
        # f_1 - keep the current 1
        # f_0 <- g * (f_0 + f_1) + f_0, g is num of zeros since last 1
        # f_1 <- f_0 + f_1
        g = 0
        f_0, f_1 = 0, 1
        while n > 0:
            d = n & 1
            if d == 0:
                g += 1
            else:
                f_1 += f_0
                f_0 += g * f_1
                g = 0
            n >>= 1
        return f_0 + f_1


if __name__ == '__main__':
    with Timer('P169'):
        p169_solver = P169Solver()
        print(p169_solver.solve())
