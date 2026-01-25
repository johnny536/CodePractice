class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if n == 1:
            return 0

        nums.sort()
        if k == n:
            return nums[n-1] - nums[0]

        max_diff = float('inf')
        for i in range(n-k+1):
            s = nums[i+k-1] - nums[i]
            if s < max_diff:
                max_diff = s

        return max_diff