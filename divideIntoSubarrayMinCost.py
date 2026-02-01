class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        nums = [nums[0]] + sorted(nums[1:])
        cost += nums[1] + nums[2]
        return cost