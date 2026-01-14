from typing import List
from collections import defaultdict

class SegTree:
    # Segment tree over x-intervals between sorted coords xs:
    # leaf i represents [xs[i], xs[i+1])
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.nseg = len(xs) - 1
        size = 4 * max(1, self.nseg)
        self.cover = [0] * size
        self.length = [0.0] * size  # covered length in this node's range

    def _pull(self, idx: int, l: int, r: int):
        if self.cover[idx] > 0:
            self.length[idx] = float(self.xs[r] - self.xs[l])
        else:
            if r - l == 1:
                self.length[idx] = 0.0
            else:
                self.length[idx] = self.length[idx * 2] + self.length[idx * 2 + 1]

    def update(self, ql: int, qr: int, delta: int):
        if ql >= qr or self.nseg <= 0:
            return
        self._update(1, 0, self.nseg, ql, qr, delta)

    def _update(self, idx: int, l: int, r: int, ql: int, qr: int, delta: int):
        if ql <= l and r <= qr:
            self.cover[idx] += delta
            self._pull(idx, l, r)
            return
        mid = (l + r) // 2
        if ql < mid:
            self._update(idx * 2, l, mid, ql, qr, delta)
        if qr > mid:
            self._update(idx * 2 + 1, mid, r, ql, qr, delta)
        self._pull(idx, l, r)

    def covered_length(self) -> float:
        return self.length[1]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        if not squares:
            return 0.0

        xs = []
        ys_set = set()
        events = defaultdict(list)  # y -> list of (x1, x2, delta)

        for x, y, l in squares:
            x1, x2 = x, x + l
            y1, y2 = y, y + l
            xs.extend([x1, x2])
            ys_set.add(y1)
            ys_set.add(y2)
            events[y1].append((x1, x2, +1))
            events[y2].append((x1, x2, -1))

        xs = sorted(set(xs))
        ys = sorted(ys_set)

        if len(xs) < 2 or len(ys) < 2:
            return float(ys[0]) if ys else 0.0

        x_index = {v: i for i, v in enumerate(xs)}

        # 1) total union area
        st = SegTree(xs)
        total = 0.0
        for i in range(len(ys) - 1):
            y = ys[i]
            for x1, x2, d in events.get(y, []):
                st.update(x_index[x1], x_index[x2], d)
            dy = ys[i + 1] - y
            if dy:
                total += st.covered_length() * dy

        half = total / 2.0
        if half == 0.0:
            return float(ys[0])

        # 2) find minimal y where area below reaches half
        st = SegTree(xs)
        below = 0.0

        for i in range(len(ys) - 1):
            y = ys[i]
            for x1, x2, d in events.get(y, []):
                st.update(x_index[x1], x_index[x2], d)

            L = st.covered_length()
            dy = ys[i + 1] - y

            # if exactly at boundary, that's the minimum
            if abs(below - half) <= 1e-12:
                return float(y)

            slab_area = L * dy
            if L > 0 and below + slab_area + 1e-15 >= half:
                t = (half - below) / L  # 0..dy
                if t < 0:
                    t = 0.0
                elif t > dy:
                    t = float(dy)
                return float(y + t)

            below += slab_area

        return float(ys[-1])