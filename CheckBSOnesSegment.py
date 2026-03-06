class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        firstZero = False
        result = True   
        for i in range(1, len(s)):
            if s[i] == '0' and not firstZero:
                firstZero = True
            if s[i] == '1' and firstZero and result:
                return False
        
        return result