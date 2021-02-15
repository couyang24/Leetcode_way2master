class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = 0
        for i in range(len(nums)):
            if target == nums[i]:
                result = i
            elif target > nums[i]:
                result = i+1
        return result
