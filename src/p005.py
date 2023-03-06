from math import log

from utils import sieve


class P005Solver:
    def solve(self, n: int = 20) -> int:
        ans = 1
        for p in sieve(n + 1)[1]:
            ans *= p ** int(log(n, p))
        return ans


if __name__ == '__main__':
    p005_solver = P005Solver()
    print(p005_solver.solve())
