class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        #Remember this
        binary_rep = format(n,'b')
        prev = '1'
        for i in range(1, len(binary_rep)):
            if binary_rep[i] == prev:
                return False
            prev = binary_rep[i]
        #True is uppercase
        return True