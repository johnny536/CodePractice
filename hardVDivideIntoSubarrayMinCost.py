class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        cost = nums[0]

        rest = sorted(enumerate(nums[1:], start=1), key=lambda x: x[1])
        arr = [(0, nums[0])] + rest

        min_idx, max_idx = 0, len(nums) - 1

        for i in range(k-1, len(nums)):
            min_idx, max_idx = min(i for i, _ in arr[1:i]), max(i for i, _ in arr[1:i])
            if max_idx - min_idx <= dist:
                cost += arr[i][1]
                for j in range(1, k-1):
                    cost += arr[j][1]
                break
        return cost