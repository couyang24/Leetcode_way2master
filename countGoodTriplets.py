class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)-3):
            for j in range(i+1, len(arr)-2):
                for k in range(j+1, len(arr)-1):
                    if (abs(arr[i] - arr[j]) <= a) & (abs(arr[j] - arr[k]) <= b) & (abs(arr[i] - arr[k]) <= c):
                        count += 1
        return count
