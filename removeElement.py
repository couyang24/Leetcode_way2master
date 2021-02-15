class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        temp = nums.copy()
        for num in temp:
            # ic(num)
            if num == val:
                nums.remove(num)
                # ic(nums)
        return len(nums)
        
