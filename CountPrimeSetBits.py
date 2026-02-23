"""
LeetCode Problem: Prime Number of Set Bits in Binary Representation

Given two integers left and right, return the count of numbers in the inclusive 
range [left, right] having a prime number of set bits in their binary representation.

A set bit refers to a '1' in the binary representation of a number.

Example 1:
Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110  (2 set bits, prime)
7  -> 111  (3 set bits, prime)
8  -> 1000 (1 set bit, not prime)
9  -> 1001 (2 set bits, prime)
10 -> 1010 (2 set bits, prime)
So the answer is 4.

Example 2:
Input: left = 10, right = 15
Output: 5

Constraints:
1 <= left <= right <= 10^6
0 <= right - left <= 10^4
"""

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for x in range(left, right + 1):
            binary_rep = format(x, 'b')
            count = binary_rep.count('1')
            # Precomputed small primes (max bits <= 20 for 10^6)
            if count in [2, 3, 5, 7, 11, 13, 17, 19]:
                res += 1
        return res


# =========================
# Test Cases
# =========================
def run_tests():
    sol = Solution()

    test_cases = [
        (6, 10, 4),
        (10, 15, 5),
        (1, 1, 0),
        (8, 8, 0),
        (15, 15, 0),  # 1111 -> 4 ones (not prime)
    ]

    for left, right, expected in test_cases:
        result = sol.countPrimeSetBits(left, right)
        print(f"Input: left={left}, right={right}")
        print(f"Expected: {expected}, Got: {result}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()