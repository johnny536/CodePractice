class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        LeetCode 696 — Count Binary Substrings

        Problem description:
        Given a binary string `s` (only '0' and '1'), return the number of
        non-empty substrings that have the same number of consecutive 0's and 1's,
        and where all the 0's and all the 1's in that substring are grouped consecutively.

        In other words, we count substrings of the form:
          "000...0111...1"  or  "111...1000...0"
        where the two groups have equal length (k zeros followed by k ones, or vice versa).

        Examples:
          s = "00110011" -> 6
          s = "10101"    -> 4

        Approach (what this solution does):
        1) Compress `s` into run-lengths of consecutive characters.
           Example: "0011100" -> [2, 3, 2]
        2) The number of valid substrings formed between adjacent runs is
           min(run[i-1], run[i]).
        3) Sum that over all adjacent pairs.

        Time:  O(n)
        Space: O(n) for the run lengths (can be optimized to O(1), but this keeps it simple)

        -----------------------
        Quick test cases
        -----------------------
        # 1) Basic examples
        # assert Solution().countBinarySubstrings("00110011") == 6
        # assert Solution().countBinarySubstrings("10101") == 4
        #
        # 2) All same character => no valid substrings
        # assert Solution().countBinarySubstrings("0000") == 0
        # assert Solution().countBinarySubstrings("111") == 0
        #
        # 3) Simple transitions
        # assert Solution().countBinarySubstrings("01") == 1        # "01"
        # assert Solution().countBinarySubstrings("10") == 1        # "10"
        # assert Solution().countBinarySubstrings("0011") == 2      # "01", "0011"
        # assert Solution().countBinarySubstrings("000111") == 3    # "01","0011","000111"
        #
        # 4) Mixed run sizes
        # assert Solution().countBinarySubstrings("00110") == 3     # "01","0011","10"
        # assert Solution().countBinarySubstrings("00011") == 2     # "01","0011"
        # assert Solution().countBinarySubstrings("01000111") == 4  # check varied runs
        """
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
        # forgot this, this is necessary!!!
        accumulate_len.append(count)
        # used for debugging
        # print(accumulate_len)

        res = 0
        for i in range(1, len(accumulate_len)):
            smaller = min(accumulate_len[i - 1], accumulate_len[i])
            res += smaller

        return res