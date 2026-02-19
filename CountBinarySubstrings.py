class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        accumulate_len = []
        prev = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                prev = s[i]
                accumulate_len.append(count)
                count = 1
        #forgot this, this is necessary!!!
        accumulate_len.append(count)
        #used for debugging
        #print(accumulate_len)

        res = 0
        for i in range(1, len(accumulate_len)):
            smaller = min(accumulate_len[i-1], accumulate_len[i])
            res += smaller
        
        return res