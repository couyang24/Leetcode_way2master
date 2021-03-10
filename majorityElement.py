class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxc = 0
        for i in set(nums):
            if nums.count(i) > maxc:
                result = i
                maxc = nums.count(i)
        return result
