class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def non_decreasing(nums):
            return all(nums[i] <= nums[i+1] for i in range(len(nums) - 1))

        count = 0
        while not non_decreasing(nums) and len(nums) != 1:
            min_sum = float("inf")
            idx = 0
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            
            # replace the pair with their sum
            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            count += 1

        return count