from utils import natural_num_sum, natural_num_squ_sum


class P006Solver:
    def solve(self, n: int = 100) -> int:
        return natural_num_sum(n) ** 2 - natural_num_squ_sum(n)


if __name__ == '__main__':
    p006_solver = P006Solver()
    print(p006_solver.solve())
