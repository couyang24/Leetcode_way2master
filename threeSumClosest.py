class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = 0
        mini = abs(sum(nums[:3]) - target)
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if abs(nums[i] + nums[j] + nums[k] - target) <= mini:
                        result = nums[i] + nums[j] + nums[k]
                        if mini == 0:
                            return result
                        mini = abs(nums[i] + nums[j] + nums[k] - target)
        return result
