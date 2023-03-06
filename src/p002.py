from utils import fibonacci_by_upper_bound

class P002Solver:
    def solve(self, u: int = 4000000) -> int:
        return sum(f for f in fibonacci_by_upper_bound(u) if f & 1 == 0)


if __name__ == '__main__':
    p002_solver = P002Solver()
    print(p002_solver.solve())
