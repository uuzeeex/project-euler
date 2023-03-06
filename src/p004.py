from utils import check_palindrome


class P004Solver:
    def solve(self) -> int:
        ans = 0
        for i in range(100, 1000):
            for j in range(i, 1000):
                if check_palindrome(i * j):
                    ans = max(ans, i * j)
        return ans


if __name__ == '__main__':
    p004_solver = P004Solver()
    print(p004_solver.solve())
