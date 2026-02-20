"""
LeetCode 761. Special Binary String (Hard)

Special binary strings are binary strings with the following two properties:
1) The number of '0's is equal to the number of '1's.
2) Every prefix of the binary string has at least as many '1's as '0's.

You are given a special binary string s.

A move consists of choosing two consecutive, non-empty, special substrings of s,
and swapping them. Two strings are consecutive if the last character of the first
string is exactly one index before the first character of the second string.

Return the lexicographically largest resulting string possible after applying
the mentioned operations on the string.

Example 1:
Input:  s = "11011000"
Output: "11100100"
Explanation: The strings "10" (at s[1]) and "1100" (at s[3]) are swapped.

Example 2:
Input:  s = "10"
Output: "10"
"""


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        Strategy (classic):
        - Parse s into top-level special chunks by balancing count(1) - count(0).
        - Each top-level chunk has the form: "1" + inner + "0".
        - Recursively maximize the inner part, then wrap back.
        - Sort the resulting top-level chunks in descending lexicographic order
          and concatenate. This yields the largest possible string.
        """
        # Split into top-level special substrings using balance counting.
        parts: list[str] = []
        balance = 0
        start = 0

        for i, ch in enumerate(s):
            balance += 1 if ch == "1" else -1
            if balance == 0:
                # s[start:i+1] is a top-level special substring: "1" + inner + "0"
                inner = s[start + 1 : i]
                parts.append("1" + self.makeLargestSpecial(inner) + "0")
                start = i + 1

        # Sort parts descending to maximize lexicographic order, then join.
        parts.sort(reverse=True)
        return "".join(parts)


def run_tests() -> None:
    sol = Solution()

    # Provided examples
    assert sol.makeLargestSpecial("11011000") == "11100100"
    assert sol.makeLargestSpecial("10") == "10"

    # Additional test cases
    # Already lexicographically largest at top-level
    assert sol.makeLargestSpecial("111000") == "111000"

    # Two top-level chunks: "10" + "10" -> same after sort
    assert sol.makeLargestSpecial("1010") == "1010"

    # Nested structure
    # "1100" is special; inside is "10" which stays "10"
    assert sol.makeLargestSpecial("1100") == "1100"

    # More complex: split into chunks and reorder
    # s = "11001100" -> top-level chunks are "1100" and "1100" -> unchanged
    assert sol.makeLargestSpecial("11001100") == "11001100"

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()