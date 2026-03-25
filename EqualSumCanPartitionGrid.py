from typing import List


class Solution:
    """
    Equal Sum Grid Partition I

    You are given an m x n matrix grid of positive integers.
    Determine if it is possible to make either:

    1. one horizontal cut, or
    2. one vertical cut

    such that:
    - both resulting sections are non-empty
    - the sum of the elements in both sections is equal

    Return True if such a partition exists, otherwise return False.

    Example 1:
        Input: grid = [[1, 4], [2, 3]]
        Output: True
        Explanation:
            A horizontal cut between row 0 and row 1 gives:
            top sum = 1 + 4 = 5
            bottom sum = 2 + 3 = 5

    Example 2:
        Input: grid = [[1, 3], [2, 4]]
        Output: False
        Explanation:
            No horizontal or vertical cut creates two non-empty parts
            with equal sums.
    """

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # 2D prefix sum array
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        total = 0

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                    + grid[i][j]
                )
                total += grid[i][j]

        if total % 2 != 0:
            return False

        half = total // 2

        # Check horizontal cuts
        # prefix[i][n] = sum of first i rows
        # valid cut means top has at least 1 row and bottom has at least 1 row
        for i in range(1, m):
            if prefix[i][n] == half:
                return True

        # Check vertical cuts
        # prefix[m][j] = sum of first j columns
        # valid cut means left has at least 1 col and right has at least 1 col
        for j in range(1, n):
            if prefix[m][j] == half:
                return True

        return False


def run_tests():
    sol = Solution()

    test_cases = [
        # Example 1
        ([[1, 4], [2, 3]], True),

        # Example 2
        ([[1, 3], [2, 4]], False),

        # Horizontal cut works
        ([[2, 2], [1, 3]], True),

        # Vertical cut works
        ([[1, 2], [1, 2]], True),

        # Single row, can only cut vertically
        ([[1, 1, 2]], True),

        # Single column, can only cut horizontally
        ([[2], [1], [1]], True),

        # Odd total sum
        ([[1, 2], [3, 5]], False),

        # No valid cut
        ([[1, 2, 3], [4, 5, 6]], False),
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        result = sol.canPartitionGrid(grid)
        print(f"Test case {i}: expected={expected}, got={result}")
        assert result == expected, f"Failed on test case {i}: {grid}"

    print("All test cases passed!")


if __name__ == "__main__":
    run_tests()