class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        def isTrionic(nums: List[int], i, j) -> bool:
            if i-j < 3:  # need 3 segments, each length >= 2
                return False

            # 1) strictly increasing: nums[i..p]
            x = i
            while i < j and nums[i] < nums[i + 1]:
                i += 1
            p = i
            if p == x or i == j:  # must have at least one increase (so p > 0)
                return False

            # 2) strictly decreasing: nums[p..q]
            while i < j and nums[i] > nums[i + 1]:
                i += 1
            q = i
            if q == p or i == j:  # must have at least one decrease (so q > p)
                return False

            # 3) strictly increasing: nums[q..n-1]
            while i < j and nums[i] < nums[i + 1]:
                i += 1

            # must end exactly at the last index, and q must be < n-1 (so last segment has length >= 2)
            return i == j and q < j
        pass