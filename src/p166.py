from typing import List

from timer import Timer
from utils import sum_digits


def _ge_down(A: List[List[float]]) -> None:
    m, n = len(A), len(A[0])
    for i in range(m - 1):
        if A[i][i] == 0:
            for j in range(i + 1, m):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    break
        for k in range(n - 1, i - 1, -1):
            A[i][k] /= A[i][i]
        for j in range(i + 1, m):
            if A[j][i] != 0:
                for k in range(n - 1, i - 1, -1):
                    A[j][k] = A[j][k] / A[j][i] - A[i][k]


def _ge_up(A: List[List[float]]) -> None:
    m, n = len(A), len(A[0])
    for i in range(m - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if A[j][i] != 0:
                for k in range(n - 1, i - 1, -1):
                    A[j][k] -= A[i][k] * A[j][i]


def _dot(v1: List[int], v2: List[int]) -> int:
    ret = 0
    for e1, e2 in zip(v1, v2):
        ret += e1 * e2
    return ret


class P166Solver:
    def solve(self):

        A = [[1, 1, 1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0],  # r1 == r2
             [1, 1, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0],  # r1 == r3
             [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1],  # r1 == r4
           # [0, 1, 1, 1, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0],   # r1 == c1, dropped as it's dependent
             [1, 0, 1, 1, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0],   # r1 == c2
             [1, 1, 0, 1, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0],   # r1 == c3
             [1, 1, 1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1],   # r1 == c4
             [0, 1, 1, 1, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1],   # r1 == d1
             [1, 1, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0]]   # r1 == d2
        # gaussian elimination down
        _ge_down(A)
        # manually swap column 7 and 8 to the left half of A identity
        for r in A:
            r[7], r[8] = r[8], r[7]
        for i in range(15, 6, -1):
            A[-1][i] /= A[-1][7]
        # gaussian elimination up
        _ge_up(A)
        # take negative of the right half
        R = [[-int(round(a)) for a in r[8:]] for r in A]

        # solve linear system y = Rx with rank 8, s.t. 0 <= x, y <= 9

        # slower dfs

        vec = [0 for _ in range(8)]

        def dfs(d: int) -> int:
            nonlocal vec
            if d == 3 and not 0 <= _dot(R[4], vec) <= 9:
                return 0
            if d == 5 and not 0 <= _dot(R[0], vec) <= 9:
                return 0
            if d == 6 and not 0 <= _dot(R[2], vec) <= 9:
                return 0
            if d == 7:
                if not 0 <= _dot(R[3], vec) <= 9:
                    return 0
                if not 0 <= _dot(R[5], vec) <= 9:
                    return 0
            if d == 8:
                if not 0 <= _dot(R[1], vec) <= 9:
                    return 0
                if not 0 <= _dot(R[6], vec) <= 9:
                    return 0
                if not 0 <= _dot(R[7], vec) <= 9:
                    return 0
                return 1
            cnt = 0
            for a in range(10):
                vec[d] = a
                cnt += dfs(d + 1)
            return cnt

        # return dfs(0)

        # faster iterative solution

        ans = 0
        for a24 in range(10):
            for a32 in range(10):
                for a33 in range(10):
                    a21 = -a24 + a32 + a33
                    if not 0 <= a21 <= 9:
                        continue
                    for a34 in range(10):
                        for a41 in range(10):
                            a11 = a24 + a34 - a41
                            if not 0 <= a11 <= 9:
                                continue
                            for a42 in range(10):
                                a13 = -a24 + a32 - a33 - a34 + 2 * a41 + a42
                                if not 0 <= a13 <= 9:
                                    continue
                                for a43 in range(10):
                                    a14 = -a24 - a34 + a41 + a42 + a43
                                    if not 0 <= a14 <= 9:
                                        continue
                                    a22 = -a24 - a33 - a34 + 2 * a41 + a42 + a43
                                    if not 0 <= a22 <= 9:
                                        continue
                                    for a44 in range(10):
                                        a12 = a24 - a32 + a33 + a34 - a41 - a42 + a44
                                        if not 0 <= a12 <= 9:
                                            continue
                                        a23 = a24 - a32 + a34 - a41 + a44
                                        if not 0 <= a23 <= 9:
                                            continue
                                        a31 = -a32 - a33 - a34 + a41 + a42 + a43 + a44
                                        if 0 <= a31 <= 9:
                                            ans += 1
        return ans


if __name__ == '__main__':
    with Timer('P166'):
        p166_solver = P166Solver()
        print(p166_solver.solve())

# garbage brute-force solution (answer even wrong!)

'''
def _fill(new_fill: int, vert_sums: List[int], diag_sums: List[int], row: int, n: int) -> None:
    for i in range(n):
        d = new_fill % 10
        vert_sums[i] += d
        if i == row:
            diag_sums[0] += d
        if i + row == n - 1:
            diag_sums[1] += d


def _empty(new_fill: int, vert_sums: List[int], diag_sums: List[int], row: int, n: int) -> None:
    for i in range(n):
        d = new_fill % 10
        vert_sums[i] -= d
        if i == row:
            diag_sums[0] -= d
        if i + row == n - 1:
            diag_sums[1] -= d

class P166Solver:
    def solve(self):
        rec = [[] for _ in range(n * 9 + 1)]
        for i in range(10 ** n):
            rec[sum_digits(i)].append(i)
        vert_sums = [0 for _ in range(n)]
        diag_sums = [0 for _ in range(2)]

        def dfs(row: int, s: int) -> int:
            nonlocal vert_sums, diag_sums
            if row == n - 1:
                return int(sum(vert_sums) == s * (n - 1))
            cnt = 0
            for new_fill in rec[s]:
                _fill(new_fill, vert_sums, diag_sums, row, n)
                if all(cur_s <= s for cur_s in [*vert_sums, *diag_sums]):
                    cnt += dfs(row + 1, s)
                _empty(new_fill, vert_sums, diag_sums, row, n)
            return cnt

        return sum([dfs(0, s) for s in range(len(rec))])
'''
