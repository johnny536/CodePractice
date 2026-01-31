class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        
        s = 0

        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] == target:
                s = mid
                break
            elif letters[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        while s < len(letters) and letters[s] <= target:
            s += 1

        if s < len(letters) and letters[s] > target:
            return letters[s]
        else:
            return letters[0]