class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            value = nums[i]
            step = i+value
            if step >= n:
                while step >= n:
                    step -= n
            elif step < -n:
                while step < -n:
                    step += n
            #print(step)
            result.append(nums[step]) #cannot use result[i]
        return result