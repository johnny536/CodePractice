class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
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