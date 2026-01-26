class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []

        min = float('inf')
        for i in range(len(arr)-1):
            s = arr[i+1] - arr[i]
            if s == min:
                res.append([arr[i], arr[i+1]])
            elif s < min:
                res.clear()
                min = s
                res.append([arr[i], arr[i+1]]) #太牛了 金子路 要继续加油阿

        return res