class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = float('-inf')
        i, r = 0, len(nums)-1
        while i < r:
            s = nums[i] + nums[r]
            if s > max_sum:
                max_sum = s
            i += 1
            r -= 1

        return max_sum