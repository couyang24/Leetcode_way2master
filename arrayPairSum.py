class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums = sorted(nums)
        for i in range(int((len(nums))/2)):
            total += nums[2*i]
        return total
