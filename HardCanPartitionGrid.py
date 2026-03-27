from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        """
        Equal Sum Grid Partition II

        You are given an m x n matrix `grid` of positive integers.
        Your task is to determine if it is possible to make either
        one horizontal or one vertical cut on the grid such that:

        1. Each of the two resulting sections formed by the cut is non-empty.
        2. The sum of elements in both sections is equal, or can be made equal
           by discounting at most one single cell in total (from either section).
        3. If a cell is discounted, the rest of that section must remain connected.

        Return `True` if such a partition exists; otherwise, return `False`.

        Note:
        A section is connected if every cell in it can be reached from any other
        cell in it by moving up, down, left, or right through other cells in the section.

        Example 1:
            Input: grid = [[1,4],[2,3]]
            Output: True
            Explanation:
            A horizontal cut after the first row gives sums 1 + 4 = 5
            and 2 + 3 = 5, which are already equal.

        Example 2:
            Input: grid = [[1,2],[3,4]]
            Output: True
            Explanation:
            A vertical cut after the first column gives sums 1 + 3 = 4
            and 2 + 4 = 6.
            By discounting 2 from the right section, both sums become 4,
            and the remaining cells stay connected.

        Example 3:
            Input: grid = [[1,2,4],[2,3,5]]
            Output: False
            Explanation:
            A horizontal cut after the first row gives sums 1 + 2 + 4 = 7
            and 2 + 3 + 5 = 10.
            Discounting 3 from the bottom section makes both sums 7,
            but the remaining bottom cells are split into [2] and [5],
            so that section is not connected.

        Example 4:
            Input: grid = [[4,1,8],[3,2,6]]
            Output: False

        Constraints:
            - 1 <= m == grid.length <= 10^5
            - 1 <= n == grid[i].length <= 10^5
            - 2 <= m * n <= 10^5
            - 1 <= grid[i][j] <= 10^5
        """
        m, n = len(grid), len(grid[0])

        total = 0
        row_sums = [0] * m
        col_sums = [0] * n

        min_row = {}
        max_row = {}
        min_col = {}
        max_col = {}

        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                total += v
                row_sums[i] += v
                col_sums[j] += v

                if v not in min_row:
                    min_row[v] = i
                    max_row[v] = i
                    min_col[v] = j
                    max_col[v] = j
                else:
                    min_row[v] = min(min_row[v], i)
                    max_row[v] = max(max_row[v], i)
                    min_col[v] = min(min_col[v], j)
                    max_col[v] = max(max_col[v], j)

        def can_remove_top(cut_row: int, diff: int) -> bool:
            rows = cut_row + 1
            cols = n

            if rows == 1 and cols == 1:
                return grid[0][0] == diff
            if rows == 1:
                return grid[0][0] == diff or grid[0][cols - 1] == diff
            if cols == 1:
                return grid[0][0] == diff or grid[cut_row][0] == diff
            return diff in min_row and min_row[diff] <= cut_row

        def can_remove_bottom(cut_row: int, diff: int) -> bool:
            start = cut_row + 1
            rows = m - start
            cols = n

            if rows == 1 and cols == 1:
                return grid[start][0] == diff
            if rows == 1:
                return grid[start][0] == diff or grid[start][cols - 1] == diff
            if cols == 1:
                return grid[start][0] == diff or grid[m - 1][0] == diff
            return diff in max_row and max_row[diff] >= start

        def can_remove_left(cut_col: int, diff: int) -> bool:
            rows = m
            cols = cut_col + 1

            if rows == 1 and cols == 1:
                return grid[0][0] == diff
            if rows == 1:
                return grid[0][0] == diff or grid[0][cut_col] == diff
            if cols == 1:
                return grid[0][0] == diff or grid[rows - 1][0] == diff
            return diff in min_col and min_col[diff] <= cut_col

        def can_remove_right(cut_col: int, diff: int) -> bool:
            start = cut_col + 1
            rows = m
            cols = n - start

            if rows == 1 and cols == 1:
                return grid[0][start] == diff
            if rows == 1:
                return grid[0][start] == diff or grid[0][n - 1] == diff
            if cols == 1:
                return grid[0][start] == diff or grid[m - 1][start] == diff
            return diff in max_col and max_col[diff] >= start

        # Try horizontal cuts
        top_sum = 0
        for i in range(m - 1):
            top_sum += row_sums[i]
            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            if top_sum > bottom_sum:
                if can_remove_top(i, top_sum - bottom_sum):
                    return True
            else:
                if can_remove_bottom(i, bottom_sum - top_sum):
                    return True

        # Try vertical cuts
        left_sum = 0
        for j in range(n - 1):
            left_sum += col_sums[j]
            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            if left_sum > right_sum:
                if can_remove_left(j, left_sum - right_sum):
                    return True
            else:
                if can_remove_right(j, right_sum - left_sum):
                    return True

        return False


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([[1, 4], [2, 3]], True),          # Example 1
        ([[1, 2], [3, 4]], True),          # Example 2
        ([[1, 2, 4], [2, 3, 5]], False),   # Example 3
        ([[4, 1, 8], [3, 2, 6]], False),   # Example 4
        ([[1, 1]], True),                  # simple vertical cut
        ([[2], [2]], True),                # simple horizontal cut
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        result = sol.canPartitionGrid(grid)
        print(f"Test case {i}: grid = {grid}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        print(f"Pass:     {result == expected}")
        print("-" * 40)