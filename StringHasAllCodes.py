"""
Check If a String Contains All Binary Codes of Size K

Problem Description:
--------------------
Given a binary string `s` and an integer `k`, return True if every binary code 
of length `k` is a substring of `s`. Otherwise, return False.

A binary code of length `k` means any possible string of length `k` made up of 
only '0' and '1'.

There are exactly 2^k possible binary codes of length k.

Examples:
---------

Example 1:
Input:  s = "00110110", k = 2
Output: True
Explanation:
All possible binary codes of length 2 are:
"00", "01", "10", "11"
They all appear as substrings of s.

Example 2:
Input:  s = "0110", k = 1
Output: True
Explanation:
Binary codes of length 1 are:
"0", "1"
Both appear in s.

Example 3:
Input:  s = "0110", k = 2
Output: False
Explanation:
Binary code "00" does not appear in s.
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        pass


def run_tests():
    solution = Solution()
    
    test_cases = [
        ("00110110", 2, True),
        ("0110", 1, True),
        ("0110", 2, False),
        ("0000000000", 3, False),  # missing many combinations
        ("11111111", 1, False),    # missing '0'
        ("1010101010", 2, False), # missing '00' and '11'
        ("1010101010", 3, False),
        ("", 1, False),
    ]
    
    passed = 0
    
    for idx, (s, k, expected) in enumerate(test_cases, 1):
        result = solution.hasAllCodes(s, k)
        print(f"Test Case {idx}: s='{s}', k={k}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 40)
        
        if result == expected:
            passed += 1
    
    print(f"Passed {passed} out of {len(test_cases)} tests.")


if __name__ == "__main__":
    run_tests()