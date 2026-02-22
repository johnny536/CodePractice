class Solution:
    def binaryGap(self, n: int) -> int:
        binary_rep = format(n, 'b')
        count = 1
        accumulated_Zero = []
        for i in range(1, len(binary_rep)):
            if binary_rep[i] == '0':
                count += 1
            else:
                accumulated_Zero.append(count)
                count = 1
        if not accumulated_Zero:
            return 0
        else:
            return max(accumulated_Zero)