class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        indexed = list(enumerate(nums))
        indexed.sort(key=lambda x: x[1])

        l, r = 0, len(nums) - 1
        while l < r:
            s = indexed[l][1] + indexed[r][1]
            if s == target:
                return [indexed[l][0], indexed[r][0]]
            if s < target:
                l += 1
            else:
                r -= 1