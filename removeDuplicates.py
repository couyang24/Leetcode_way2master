class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dct = {}
        temp = nums.copy()
        for num in temp:
            if num in dct.keys():
                nums.remove(num)
            else:
                dct[num] = True
        # ic(dct)
        return len(dct.keys())
