"""
Sort Integers by The Number of 1 Bits

Problem Description:
--------------------
You are given an integer array arr.

Sort the integers in the array in ascending order by the number of 1's 
in their binary representation.

If two or more integers have the same number of 1's, sort them in ascending order.

Return the array after sorting it.


Example 1:
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]

Explanation:
0 has 0 bits.
1,2,4,8 have 1 bit.
3,5,6 have 2 bits.
7 has 3 bits.


Example 2:
Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
"""

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


# ==========================
# Test Cases
# ==========================

def run_tests():
    sol = Solution()

    test_cases = [
        # Example 1
        ([0,1,2,3,4,5,6,7,8], [0,1,2,4,8,3,5,6,7]),

        # Example 2
        ([1024,512,256,128,64,32,16,8,4,2,1],
         [1,2,4,8,16,32,64,128,256,512,1024]),

        # Single element
        ([5], [5]),

        # With duplicates
        ([3,3,1,2], [1,2,3,3]),

        # Random case
        ([10,100,1000,7], sorted([10,100,1000,7],
                                  key=lambda x: (bin(x).count('1'), x)))
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = sol.sortByBits(arr)
        print(f"Test Case {i}:")
        print("Input:   ", arr)
        print("Output:  ", result)
        print("Expected:", expected)
        print("Pass:", result == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()