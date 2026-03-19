from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        """
        3212. Count Submatrices With Equal Frequency of X and Y

        Given a 2D character matrix `grid`, where each cell is one of:
            - 'X'
            - 'Y'
            - '.'

        Return the number of submatrices that contain:
            1. grid[0][0]
            2. an equal frequency of 'X' and 'Y'
            3. at least one 'X'

        Notes:
        - A submatrix is any contiguous rectangular region.
        - The submatrix must include the top-left cell grid[0][0].

        Example 1:
            Input:  grid = [["X","Y","."],["Y",".","."]]
            Output: 3

        Example 2:
            Input:  grid = [["X","X"],["X","Y"]]
            Output: 0

        Example 3:
            Input:  grid = [[".","."],[".","."]]
            Output: 0
        """
        m, n = len(grid), len(grid[0])
        
        # prefix sum for converted values:
        # X -> 1, Y -> -1, . -> 0
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        # prefix count of X
        x_prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                is_x = 1 if grid[i][j] == 'X' else 0
                
                prefix[i + 1][j + 1] = (
                    prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                    + val
                )
                
                x_prefix[i + 1][j + 1] = (
                    x_prefix[i][j + 1]
                    + x_prefix[i + 1][j]
                    - x_prefix[i][j]
                    + is_x
                )
                
                # submatrix must contain grid[0][0], so we only check prefix submatrices
                if prefix[i + 1][j + 1] == 0 and x_prefix[i + 1][j + 1] > 0:
                    ans += 1
        
        return ans


def main():
    """
    Test cases for the problem
    """

    sol = Solution()

    # Test case 1
    grid1 = [["X", "Y", "."], ["Y", ".", "."]]
    expected1 = 3
    print("Test 1:", sol.numberOfSubmatrices(grid1), "Expected:", expected1)

    # Test case 2
    grid2 = [["X", "X"], ["X", "Y"]]
    expected2 = 0
    print("Test 2:", sol.numberOfSubmatrices(grid2), "Expected:", expected2)

    # Test case 3
    grid3 = [[".", "."], [".", "."]]
    expected3 = 0
    print("Test 3:", sol.numberOfSubmatrices(grid3), "Expected:", expected3)


if __name__ == "__main__":
    main()