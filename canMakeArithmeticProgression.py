class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        step = (max(arr)-min(arr))/(len(arr)-1)
        num = min(arr)
        while num < max(arr):
            if num not in arr:
                return False
            num += step
        return True
        
