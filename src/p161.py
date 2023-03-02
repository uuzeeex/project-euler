from functools import cache
from typing import Tuple


class P161Solver:
    def solve(self, w: int = 9, h: int = 12) -> int:
        empty = 0
        full = (1 << w) - 1

        @cache
        def occupy(pos: int, r: int) -> Tuple[bool, int]:
            mask = 1 << pos
            return r & mask == 0, r | mask

        @cache
        def dfs(left: int, r1: int, r2: int, r3: int) -> int:
            if left == 0:
                return 1
            if r1 == full:
                return dfs(left - 1, r2, r3, empty)
            pos = 0
            while r1 & (1 << pos) != 0:
                pos += 1

            cnt = 0

            if pos < w - 1 and left > 1:
                # **
                # *
                a1, nr1 = occupy(pos, r1)
                a2, nr1 = occupy(pos + 1, nr1)
                a3, nr2 = occupy(pos + 1, r2)
                if a1 and a2 and a3:
                    cnt += dfs(left, nr1, nr2, r3)

                # **
                #  *
                a1, nr1 = occupy(pos, r1)
                a2, nr1 = occupy(pos + 1, nr1)
                a3, nr2 = occupy(pos, r2)
                if a1 and a2 and a3:
                    cnt += dfs(left, nr1, nr2, r3)

                #  *
                # **
                a1, nr1 = occupy(pos, r1)
                a2, nr2 = occupy(pos, r2)
                a3, nr2 = occupy(pos + 1, nr2)
                if a1 and a2 and a3:
                    cnt += dfs(left, nr1, nr2, r3)

            if pos > 0 and left > 1:
                # *
                # **
                a1, nr1 = occupy(pos, r1)
                a2, nr2 = occupy(pos, r2)
                a3, nr2 = occupy(pos - 1, nr2)
                if a1 and a2 and a3:
                    cnt += dfs(left, nr1, nr2, r3)

            if left > 2:
                # *
                # *
                # *
                a1, nr1 = occupy(pos, r1)
                a2, nr2 = occupy(pos, r2)
                a3, nr3 = occupy(pos, r3)
                if a1 and a2 and a3:
                    cnt += dfs(left, nr1, nr2, nr3)

            if pos < w - 2:
                # ***
                a1, nr1 = occupy(pos, r1)
                a2, nr1 = occupy(pos + 1, nr1)
                a3, nr1 = occupy(pos + 2, nr1)
                if a1 and a2 and a3:
                    cnt += dfs(left, nr1, r2, r3)

            return cnt

        return dfs(h, empty, empty, empty)


if __name__ == '__main__':
    p161_solver = P161Solver()
    print(p161_solver.solve())
