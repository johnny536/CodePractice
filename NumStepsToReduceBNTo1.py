class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        decimal = int(s,2)
        while decimal != 1:
            if decimal % 2 == 0:
                #Need to use // (integer division) instead of / (float division)
                decimal = decimal // 2
            else:
                decimal += 1
            count += 1

        return count