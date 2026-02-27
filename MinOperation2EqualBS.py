"""
Minimum Operations to Equalize Binary String

You are given:
- a binary string s (only contains '0' and '1')
- an integer k

In ONE operation, you must:
- choose EXACTLY k different indices in s
- flip each chosen character:
    '0' -> '1'
    '1' -> '0'

Goal:
Return the minimum number of operations required to make ALL characters in s equal to '1'.
If it is not possible, return -1.

Examples:
1) s = "110", k = 1  -> 1
2) s = "0101", k = 3 -> 2
3) s = "101", k = 2  -> -1
"""

from typing import *


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # TODO: implement
        pass


# -------------------------
# Test cases (run `python filename.py`)
# -------------------------
def run_tests():
    sol = Solution()

    tests = [
        # Provided examples
        ("110", 1, 1),
        ("0101", 3, 2),
        ("101", 2, -1),

        # Edge-ish / sanity tests (expected values depend on correct implementation)
        ("1", 1, 0),       # already all '1'
        ("0", 1, 1),       # flip the only bit
        ("1111", 2, 0),    # already all '1'

        # More cases
        ("00", 2, 1),      # flip both -> "11"
        ("01", 2, -1),     # flip both: "01"->"10" not all ones; stuck in 2-cycle, so impossible
        ("000", 2, -1),    # typically impossible with exactly-2 flips on length-3 to reach "111"
        ("0000", 2, 2),    # flip pairs twice can reach all ones
        ("010", 1, 2),     # flip two zeros individually
    ]

    for i, (s, k, expected) in enumerate(tests, 1):
        got = sol.minOperations(s, k)
        ok = (got == expected)
        print(f"Test {i}: s={s!r}, k={k} -> got {got}, expected {expected} | {'PASS' if ok else 'FAIL'}")

    print("\nNote: Some non-example expectations above assume standard reasoning; if your final algorithm disagrees,")
    print("double-check those specific cases (or remove them and keep only the official examples).")


if __name__ == "__main__":
    run_tests()