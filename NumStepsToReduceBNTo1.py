"""
Number of Steps to Reduce a Number in Binary Representation to One

Problem Description:
Given the binary representation of an integer as a string s, return the number of steps
to reduce it to 1 under the following rules:

- If the current number is even, you have to divide it by 2.
- If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

Examples:
Input:  s = "1101"   (13 in decimal)
Output: 6

Input:  s = "10"     (2 in decimal)
Output: 1

Input:  s = "1"      (1 in decimal)
Output: 0
"""

from typing import List, Tuple


class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        decimal = int(s, 2)
        while decimal != 1:
            if decimal % 2 == 0:
                # Need to use // (integer division) instead of / (float division)
                decimal = decimal // 2
            else:
                decimal += 1
            count += 1
        return count


# ----------------------------
# Test Cases (run this file)
# ----------------------------
def run_tests():
    sol = Solution()

    # (input, expected)
    tests: List[Tuple[str, int]] = [
        ("1", 0),          # already 1
        ("10", 1),         # 2 -> 1
        ("11", 3),         # 3 -> 4 -> 2 -> 1
        ("1101", 6),       # example: 13 -> ... -> 1 (6 steps)
        ("101", 5),        # 5 -> 6 -> 3 -> 4 -> 2 -> 1
        ("111", 4),        # 7 -> 8 -> 4 -> 2 -> 1
        ("1000", 3),       # 8 -> 4 -> 2 -> 1
        ("1111", 5),       # 15 -> 16 -> 8 -> 4 -> 2 -> 1
    ]

    for s, expected in tests:
        got = sol.numSteps(s)
        assert got == expected, f"FAIL: s={s}, expected={expected}, got={got}"
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()