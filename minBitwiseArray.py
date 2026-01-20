class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for p in nums:
            # If p is even, impossible
            if p % 2 == 0:
                ans.append(-1)
                continue

            # Count trailing 1s
            s = 0
            temp = p
            while temp & 1:
                s += 1
                temp >>= 1

            # Minimum x
            x = p - (1 << (s - 1))
            ans.append(x)

        return ans