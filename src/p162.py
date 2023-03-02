class P162Solver:
    def solve(self, n_digits: int = 16) -> str:
        # when 0, 1, A only (wrong understanding)
        # return '%X' % (3 ** n_digits - 3 * 2 ** n_digits - 4 * 2 ** (n_digits - 2) + 2 * n_digits + 3)
        # return '%X' % sum(((3 ** i - 2 ** (i + 1) + 1) << 1) for i in range(2, n_digits))
        f = [[0 for _ in range(8)] for _ in range(2)]
        f[0][0], f[0][1], f[0][2], f[0][4] = 13, 1, 1, 1
        deduct = 0
        for i in range(1, n_digits):
            deduct += f[(i - 1) & 1][3]
            for j in range(8):
                f[i & 1][j] = 13 * f[(i - 1) & 1][j]
                if j & 1 != 0:
                    f[i & 1][j] += f[(i - 1) & 1][j] + f[(i - 1) & 1][j - 1]
                if j & 2 != 0:
                    f[i & 1][j] += f[(i - 1) & 1][j] + f[(i - 1) & 1][j - 2]
                if j & 4 != 0:
                    f[i & 1][j] += f[(i - 1) & 1][j] + f[(i - 1) & 1][j - 4]
        print(f[(n_digits - 1) & 1][7], deduct)
        return '%X' % (f[(n_digits - 1) & 1][7] - deduct)


if __name__ == '__main__':
    p162_solver = P162Solver()
    print(p162_solver.solve())
