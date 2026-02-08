class Solution:
    def minimumDeletions(self, s: str) -> int:
        idx_a = s.find('a')
        idx_firstb = s.find('b')
        if idx_firstb == -1 or idx_a == -1:
            return 0

        minDel = float('inf')
        n = len(s)

        # prefix_b[i] = number of 'b' in s[0:i]
        prefix_b = [0] * (n + 1)
        for i in range(n):
            prefix_b[i + 1] = prefix_b[i] + (s[i] == 'b')

        # suffix_a[i] = number of 'a' in s[i:n]
        suffix_a = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_a[i] = suffix_a[i + 1] + (s[i] == 'a')

        for i in range(idx_firstb, n+1): #这里必须是n+1，因为要考虑删除所有b的情况
            cost = prefix_b[i] + suffix_a[i]
            if cost < minDel:
                minDel = cost

        return minDel