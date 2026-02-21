class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for x in range(left, right+1):
            binary_rep = format(x, 'b')
            count = binary_rep.count('1')
            if count in [2, 3, 5, 7, 11, 13, 17,19]:
                res += 1

        return res