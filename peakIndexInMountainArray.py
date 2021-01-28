class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                count += 1
        return count
