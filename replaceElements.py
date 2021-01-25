class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)-1):
            max = 0
            for j in range(i+1, len(arr)):
                if arr[j]>max:
                    max = arr[j]
            result.append(max)
        result.append(-1)
        return result

# Alt
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = arr[-1]
        result = arr.copy()
        result[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            result[i] = max
            if arr[i]>max:
                max = arr[i]
        return result
