class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        You are given a string s consisting only of the characters 'a', 'b', and 'c'.

        A substring of s is called balanced if all distinct characters in the substring
        appear the same number of times.

        Return the length of the longest balanced substring of s.

        Examples:
            Example 1:
                Input:  s = "abbac"
                Output: 4
                Explanation:
                    The longest balanced substring is "abba" because both distinct characters
                    'a' and 'b' each appear exactly 2 times.

            Example 2:
                Input:  s = "aabcc"
                Output: 3
                Explanation:
                    The longest balanced substring is "abc" because all distinct characters
                    'a', 'b', and 'c' each appear exactly 1 time.

            Example 3:
                Input:  s = "aba"
                Output: 2
                Explanation:
                    One of the longest balanced substrings is "ab" because both distinct
                    characters 'a' and 'b' each appear exactly 1 time.
                    Another longest balanced substring is "ba".
        """
        # TODO: implement
        n = len(s)

        max_run_1 = 0
        max_run_2 = 0
        max_run_3 = 0

        # -------------------------
        # Case 1: only one character
        # -------------------------
        curr = 0
        prev = 'd'

        for ch in s:
            if ch == prev:
                curr += 1
            else:
                curr = 1
                prev = ch
            max_run_1 = max(max_run_1, curr)

        # -----------------------------------------
        # Case 2: exactly two distinct characters
        # -----------------------------------------
        def best_two(x: str, y: str) -> int:
            best = 0
            diff = 0
            # first_seen[diff] = earliest index where this diff occurred
            # within the current segment that contains only x/y.
            first_seen: Dict[int, int] = {0: -1}

            for i, ch in enumerate(s):
                if ch == x:
                    diff += 1
                elif ch == y:
                    diff -= 1
                else:
                    # third character breaks validity for this pair -> reset segment
                    diff = 0
                    first_seen = {0: i}
                    continue

                if diff in first_seen:
                    best = max(best, i - first_seen[diff])
                else:
                    first_seen[diff] = i
            return best

        max_run_2 = max(best_two('a','b'), best_two('b','c'), best_two('a','c'))

        # -----------------------------------------
        # Case 3: all three characters (a, b, c)
        # -----------------------------------------
        ca = cb = cc = 0
        # state = (cb - ca, cc - ca)
        state_first: Dict[tuple[int, int], int] = {(0, 0): -1}
        for i, ch in enumerate(s):
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:  # 'c'
                cc += 1

            state = (cb - ca, cc - ca)
            if state in state_first:
                max_run_3 = max(max_run_3, i - state_first[state])
            else:
                state_first[state] = i
        
        return max(max_run_1, max_run_2, max_run_3)