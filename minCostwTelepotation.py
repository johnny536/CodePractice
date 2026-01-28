from typing import List
from math import inf

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        N = m * n
        INF = 10**18

        # Flatten grid values
        vals_flat = [grid[i][j] for i in range(m) for j in range(n)]

        # Coordinate-compress values (for fast ">= current value" suffix-min queries)
        uniq = sorted(set(vals_flat))
        idx_of = {v: i for i, v in enumerate(uniq)}
        D = len(uniq)
        val_idx = [idx_of[v] for v in vals_flat]

        # dp_prev[pos] = min cost to be at cell 'pos' using exactly t teleports (t in current loop)
        dp_prev = [INF] * N
        dp_prev[0] = 0

        # t = 0 (no teleports): standard grid DP (only right/down, pay destination value)
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                if pos == 0:
                    continue
                best = INF
                if i > 0:
                    best = min(best, dp_prev[pos - n] + grid[i][j])
                if j > 0:
                    best = min(best, dp_prev[pos - 1] + grid[i][j])
                dp_prev[pos] = best

        # t = 1..k
        for _ in range(1, k + 1):
            # best_at_value[idx] = min dp_prev[pos] among cells whose grid value == uniq[idx]
            best_at_value = [INF] * D
            for pos in range(N):
                d = dp_prev[pos]
                if d < best_at_value[val_idx[pos]]:
                    best_at_value[val_idx[pos]] = d

            # suf[idx] = min cost among ALL cells with value >= uniq[idx]
            suf = [INF] * D
            cur = INF
            for i in range(D - 1, -1, -1):
                if best_at_value[i] < cur:
                    cur = best_at_value[i]
                suf[i] = cur

            # dp_cur: compute row-major; allow either:
            # 1) arrive by teleport (cost = suf[value_idx], does NOT pay destination cell)
            # 2) arrive from top/left (pay destination cell)
            dp_cur = [INF] * N
            dp_cur[0] = 0

            for i in range(m):
                for j in range(n):
                    pos = i * n + j
                    if pos == 0:
                        continue
                    best = suf[val_idx[pos]]  # teleport into (i,j) for free if reachable somewhere before
                    if i > 0:
                        best = min(best, dp_cur[pos - n] + grid[i][j])
                    if j > 0:
                        best = min(best, dp_cur[pos - 1] + grid[i][j])
                    dp_cur[pos] = best

            dp_prev = dp_cur

        return dp_prev[N - 1]