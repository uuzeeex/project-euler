from collections import deque
from typing import List

from timer import Timer


def _gen_init_ulams(n: int) -> List[int]:
    a, b = 2, n * 2 + 1
    ulam_set = {a, b}
    ulam_seq = [a, b]
    i = b + 1
    while True:
        cnt = 0
        for u in reversed(ulam_seq):
            if i - u >= u:
                break
            if i - u in ulam_set:
                cnt += 1
                if cnt > 1:
                    break
        if cnt == 1:
            ulam_set.add(i)
            ulam_seq.append(i)
            if i > 2 and i & 1 == 0:
                break
        i += 1
    return ulam_seq


def _gen_odd_ulams(init_ulam: List[int], k: int) -> List[int]:
    e1, e2 = init_ulam[0], init_ulam[-1]
    cur = e2 + 1
    q = deque(init_ulam[1: -1])
    odd_ulam = []
    for i in range(k):
        while not (cur - e1 == q[-1]) ^ (cur - e2 == q[0]):
            cur += 2
            if cur - q[0] > e2:
                q.popleft()
        q.append(cur)
        odd_ulam.append(cur)
        cur += 2
        if cur - q[0] > e2:
            q.popleft()
    return odd_ulam


def _check_period(odd_ulams: List[int], t: int) -> bool:
    p = t
    while p < len(odd_ulams) and odd_ulams[p] == odd_ulams[p % t]:
        p += 1
    return p == len(odd_ulams)


def _calc_rep_diffs(init_ulam: List[int]) -> List[int]:
    k = 64
    p = 1
    while True:
        odd_ulams = _gen_odd_ulams(init_ulam, k)
        diffs = [odd_ulams[i] - odd_ulams[i - 1] for i in range(1, len(odd_ulams))]
        while p * 2 <= k:
            if _check_period(diffs, p):
                return diffs[: p]
            p += 1
        k *= 2


def _get_ulam_in_rep(u_0: int, rep_diffs: List[int], k: int) -> int:
    t = len(rep_diffs)
    return u_0 + sum(rep_diffs) * (k // t) + sum(rep_diffs[: k % t])


class P167Solver:
    def solve(self, k: int = 10 ** 11) -> int:
        ans = 0
        for n in range(2, 11):
            init_ulams = _gen_init_ulams(n)
            rep_diffs = _calc_rep_diffs(init_ulams)
            ans += _get_ulam_in_rep(_gen_odd_ulams(init_ulams, 1)[0], rep_diffs, k - len(init_ulams) - 1)
        return ans


if __name__ == '__main__':
    with Timer('P167'):
        p167_solver = P167Solver()
        print(p167_solver.solve())
