class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if len(nums) == 0:
            return []
        start = nums[0]
        for i in range(1, len(nums)):
            check = True
            if nums[i]-1 != nums[i-1]:
                if nums[i-1] == start:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        if start == nums[-1]:
            result.append(f"{start}")
        else:
            result.append(f"{start}->{nums[-1]}")
        return result
