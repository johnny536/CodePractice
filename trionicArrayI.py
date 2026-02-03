class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:  # need 3 segments, each length >= 2
            return False

        i = 0

        # 1) strictly increasing: nums[0..p]
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        p = i
        if p == 0:  # must have at least one increase (so p > 0)
            return False

        # 2) strictly decreasing: nums[p..q]
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        q = i
        if q == p:  # must have at least one decrease (so q > p)
            return False

        # 3) strictly increasing: nums[q..n-1]
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # must end exactly at the last index, and q must be < n-1 (so last segment has length >= 2)
        result = 100
        return i == n - 1 and q < n - 1 