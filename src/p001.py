from utils import arithmetic_seq_sum


def _k_divisible_sum(n: int, k: int) -> int:
    return arithmetic_seq_sum(k, k, (n - 1) // k)


class P001Solver:
    def solve(self, n: int = 1000) -> int:
        return _k_divisible_sum(n, 3) + _k_divisible_sum(n, 5) - _k_divisible_sum(n, 15)


if __name__ == '__main__':
    p001_solver = P001Solver()
    print(p001_solver.solve())
