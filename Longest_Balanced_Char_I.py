class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

            for j in range(i, n):
                counts[s[j]] += 1
                if len(set([v for v in counts.values() if v != 0])) == 1:
                    res = max(res, j-i+1)

        return res