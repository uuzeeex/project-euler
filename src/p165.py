from utils import blum_blum_shub, true_intersection, Segment, Point, intersection


class P165Solver:
    def solve(self, n: int = 5000):
        segs, ts = [], []
        true_intersections = set()
        for t in blum_blum_shub(n << 2):
            ts.append(t)
            if len(ts) & 3 != 0:
                continue
            new_seg = Segment(Point(ts[-4], ts[-3]), Point(ts[-2], ts[-1]))
            for seg in segs:
                if true_intersection(new_seg, seg):
                    true_intersections.add(intersection(new_seg, seg))
            segs.append(new_seg)
        return len(true_intersections)


if __name__ == '__main__':
    p165_solver = P165Solver()
    print(p165_solver.solve())
