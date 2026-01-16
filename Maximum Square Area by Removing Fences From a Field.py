from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        # Add the unremovable boundary fences and sort
        hs = sorted(set(hFences + [1, m]))
        vs = sorted(set(vFences + [1, n]))

        def all_differences(arr: List[int]) -> set:
            """All possible segment lengths obtainable by removing internal fences."""
            diffs = set()
            L = len(arr)
            for i in range(L):
                ai = arr[i]
                for j in range(i + 1, L):
                    diffs.add(arr[j] - ai)
            return diffs

        # Compute all possible heights and widths
        # (Compute the smaller one as a set if you want to reduce memory; here both are similar.)
        hdiffs = all_differences(hs)

        best = 0
        L = len(vs)
        for i in range(L):
            vi = vs[i]
            for j in range(i + 1, L):
                d = vs[j] - vi
                if d in hdiffs and d > best:
                    best = d

        if best == 0:
            return -1
        return (best * best) % MOD