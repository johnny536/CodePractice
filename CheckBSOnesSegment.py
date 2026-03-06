class Solution:
    """
    LeetCode 1784. Check if Binary String Has at Most One Segment of Ones

    Question Description:
    Given a binary string `s` without leading zeros, return True if `s`
    contains at most one contiguous segment of ones. Otherwise, return False.

    A contiguous segment of ones means all the '1's appear together in one block.

    Example 1:
    Input: s = "1001"
    Output: False
    Explanation: The ones are separated into two segments.

    Example 2:
    Input: s = "110"
    Output: True

    Constraints:
    - 1 <= len(s) <= 100
    - s[i] is either '0' or '1'
    - s[0] == '1'
    """

    def checkOnesSegment(self, s: str) -> bool:
        firstZero = False
        result = True
        for i in range(1, len(s)):
            if s[i] == '0' and not firstZero:
                firstZero = True
            if s[i] == '1' and firstZero and result:
                return False
        return result


# Auto-check test cases
def run_tests():
    sol = Solution()
    
    test_cases = [
        ("1", True),
        ("11", True),
        ("110", True),
        ("111000", True),
        ("1000", True),
        ("1001", False),
        ("101", False),
        ("110011", False),
        ("101000", False),
        ("1110111", False),
    ]

    all_passed = True

    for i, (s, expected) in enumerate(test_cases, 1):
        actual = sol.checkOnesSegment(s)
        passed = actual == expected
        if not passed:
            all_passed = False

        print(f"Test {i}: s = '{s}'")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        print(f"Result:   {'PASS' if passed else 'FAIL'}")
        print("-" * 30)

    print("Final Result:", "ALL TESTS PASSED" if all_passed else "SOME TESTS FAILED")


run_tests()