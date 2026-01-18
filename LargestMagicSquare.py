from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        Kmax = min(m, n)

        # Row prefix: row_ps[r][c+1] = sum(grid[r][0..c])
        row_ps = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            s = 0
            for c in range(n):
                s += grid[r][c]
                row_ps[r][c + 1] = s

        # Col prefix: col_ps[r+1][c] = sum(grid[0..r][c])
        col_ps = [[0] * n for _ in range(m + 1)]
        for c in range(n):
            s = 0
            for r in range(m):
                s += grid[r][c]
                col_ps[r + 1][c] = s

        # Main diagonal prefix (top-left -> bottom-right):
        # d1[r+1][c+1] = sum of grid along main diag ending at (r,c)
        d1 = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                d1[r + 1][c + 1] = d1[r][c] + grid[r][c]

        # Anti-diagonal prefix (top-right -> bottom-left):
        # d2[r+1][c] = sum along anti diag ending at (r,c) when indexing d2 with shifted cols
        # We'll store with one extra column on both sides: size (m+1) x (n+2)
        d2 = [[0] * (n + 2) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                d2[r + 1][c + 1] = d2[r][c + 2] + grid[r][c]

        def row_sum(r: int, c: int, k: int) -> int:
            return row_ps[r][c + k] - row_ps[r][c]

        def col_sum(r: int, c: int, k: int) -> int:
            return col_ps[r + k][c] - col_ps[r][c]

        def main_diag_sum(r: int, c: int, k: int) -> int:
            # from (r,c) to (r+k-1, c+k-1)
            return d1[r + k][c + k] - d1[r][c]

        def anti_diag_sum(r: int, c: int, k: int) -> int:
            # from (r,c+k-1) to (r+k-1, c)
            # using d2: d2[r+1][c+1] = d2[r][c+2] + grid[r][c]
            # sum from (r,c+k-1) downward-left length k:
            # end at (r+k-1, c), so use indices:
            return d2[r + k][c + 1] - d2[r][c + k + 1]

        def is_magic(r: int, c: int, k: int) -> bool:
            target = row_sum(r, c, k)

            # diagonals
            if main_diag_sum(r, c, k) != target:
                return False
            if anti_diag_sum(r, c, k) != target:
                return False

            # rows
            for rr in range(r, r + k):
                if row_sum(rr, c, k) != target:
                    return False

            # cols
            for cc in range(c, c + k):
                if col_sum(r, cc, k) != target:
                    return False

            return True

        # Try larger k first; return immediately when found.
        for k in range(Kmax, 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        return 1