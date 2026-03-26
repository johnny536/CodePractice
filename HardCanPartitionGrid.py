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
        pass


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