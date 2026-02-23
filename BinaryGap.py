"""
LeetCode Problem: Binary Gap

Given a positive integer n, return the longest distance between two adjacent 1's 
in the binary representation of n. If there are fewer than two 1's, return 0.

The distance between two adjacent 1's is the number of positions between them.

Example 1:
Input: n = 22
Output: 2
Explanation:
22 in binary is "10110".
The two adjacent 1's with the longest distance are in positions 0 and 2.
Distance = 2.

Example 2:
Input: n = 8
Output: 0
Explanation:
8 in binary is "1000".
There is only one '1', so return 0.

Example 3:
Input: n = 5
Output: 2
Explanation:
5 in binary is "101".
Distance between the two 1's is 2.

Constraints:
1 <= n <= 10^9
"""

class Solution:
    def binaryGap(self, n: int) -> int:
        binary_rep = format(n, 'b')
        count = 1
        accumulated_Zero = []

        for i in range(1, len(binary_rep)):
            if binary_rep[i] == '0':
                count += 1
            else:
                accumulated_Zero.append(count)
                count = 1

        if not accumulated_Zero:
            return 0
        else:
            return max(accumulated_Zero)