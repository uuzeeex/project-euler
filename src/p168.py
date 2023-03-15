from timer import Timer
from utils import div_to_inf_decimal


# def _r_rotate(n: int) -> int:
#     u = n % 10
#     d = 0
#     while 10 ** d <= n:
#         d += 1
#     return u * 10 ** (d - 1) + n // 10


class P168Solver:
    def solve(self, d: int = 100, trunc: int = 5) -> int:

        # for i in range(10, 10 ** 8):
        #     if _r_rotate(i) % i == 0:
        #         print(i)

        trunc_mod = 10 ** trunc

        def calc_sum(loop: int) -> int:
            res = 0
            l_loop, base = 0, 1
            while base <= loop:
                base *= 10
                l_loop += 1
            num_non_trunc = 0
            stack = loop
            while stack < trunc_mod and stack < 10 ** d:
                res = (res + stack) % trunc_mod
                num_non_trunc += 1
                stack = stack * base + loop
            res = (res + (stack % trunc_mod) * (d // l_loop - num_non_trunc)) % trunc_mod
            return res

        s = 0

        for k in range(1, 10):
            for u in range(1, 10):
                div = div_to_inf_decimal(u, 10 * k - 1)
                # what a tricky case man
                if div.int_part == 1:
                    s += calc_sum(9)
                if div.int_part == 0 and div.loop_start is not None and div.loop_start == 0:
                    n = int(''.join(map(str, div.digits)))
                    m = int(''.join(map(str, [div.digits[-1], *div.digits[: -1]])))
                    if m >= n:
                        # print(f'k = {k}, u = {u}: {div}')
                        # print(f'{n}: {calc_sum(n)}')
                        s += calc_sum(n)

        return s % trunc_mod


if __name__ == '__main__':
    with Timer('P168'):
        p168_solver = P168Solver()
        print(p168_solver.solve() - p168_solver.solve(1))
