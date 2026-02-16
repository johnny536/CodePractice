class Solution:
    def reverseBits(self, n: int) -> int:
        
        # Convert the integer to a 32-bit binary string
        binary = format(n, '032b')
        reverse_b = []

        i = 31
        while i >= 0:
            reverse_b.append(str(binary[i]))
            i -= 1
        
        # Join the reversed bits and convert back to an integer
        return int("".join(reverse_b), 2)