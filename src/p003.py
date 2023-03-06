from math import sqrt


class P003Solver:
    def solve(self, n: int = 600851475143) -> int:
        u = int(sqrt(n))
        for i in [2, *range(3, u + 1, 2)]:
            while n % i == 0:
                n //= i
            if n == 1:
                return i
        return n


if __name__ == '__main__':
    p003_solver = P003Solver()
    print(p003_solver.solve())
