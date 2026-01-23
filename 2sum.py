class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        indexed = list(enumerate(nums))
        indexed.sort(key=lambda x: x[1])
        index = 0
        for i in range(n-1):
            if indexed[i][1] + indexed[i+1][1] == target:
                index = i
                break

        return [indexed[i][0], indexed[i+1][0]]