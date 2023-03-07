class P164Solver:
    def solve(self, n: int = 20) -> int:
        f = [[[init_val for _ in range(10 - i)] for i in range(10)] for init_val in [0, 1]]
        for d in range(2, n):
            for i in range(10):
                for j in range(10 - i):
                    f[d & 1][i][j] = 0
            for i in range(10):
                for j in range(10 - i):
                    for k in range(10 - i - j):
                        f[d & 1][k][i] += f[(d - 1) & 1][i][j]
        return sum([f[(n - 1) & 1][i][j] for i in range(1, 10) for j in range(10 - i)])


if __name__ == '__main__':
    p164_solver = P164Solver()
    print(p164_solver.solve())
