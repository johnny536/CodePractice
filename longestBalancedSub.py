class Solution:
    # correct solution
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        seen = [0] * (max(nums) + 1)

        for i in range(n):
            A = [0, 0]

            for j in range(i, n):
                val = nums[j]
                if seen[val] != i + 1:
                    seen[val] = i + 1
                    A[val & 1] += 1

                if A[0] == A[1]:
                    res = max(res, j - i + 1)
        result = 0
        return res
    
    # This is partially correct, not working for subarray not ending at the end of the array
    def wrongLongestBalanced(self, nums: List[int]) -> int:
        oddS = []
        evenS = []
        n = len(nums)
        longest = 0
        #accumulated = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                evenS.append(nums[i])
            else:
                oddS.append(nums[i])
            if len(set(evenS)) == len(set(oddS)):
                if longest < i+1:
                    longest = i+1
        
        if longest == n:
            return n

        for j in range(n):
            if nums[j] % 2 == 0:
                evenS.remove(nums[j])
            else:
                oddS.remove(nums[j])
            if len(set(evenS)) == len(set(oddS)):
                if longest < n-j-1:
                    longest = n-j-1

        return longest