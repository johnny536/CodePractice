from typing import List

"""
Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length
of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSub = float('inf')
        currentSum = 0
        currentC = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            currentC += 1
            if currentSum >= target and currentC == 1:
                return 1
            while currentSum >= target:
                if currentSum >= target and currentC < minSub:
                    minSub = currentC
                currentSum -= nums[i-currentC+1]
                currentC -= 1
                
        if minSub == float('inf'):
            return 0
        return minSub


# Test cases
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)
    ]

    all_passed = True

    for i, (target, nums, expected) in enumerate(test_cases, 1):
        result = sol.minSubArrayLen(target, nums)

        if result != expected:
            all_passed = False
            print(f"Test case {i} failed: Expected {expected}, Got {result}")

    if all_passed:
        print("All test cases passed!")