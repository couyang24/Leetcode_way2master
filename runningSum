from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union

nums1 = [1, 2, 3, 4]
nums2 = [1, 1, 1, 1, 1]
nums3 = [3, 1, 2, 10, 1]
nums_lst = [nums1, nums2, nums3]


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        result = 0
        for i in range(len(nums)):
            result += nums[i]
            lst.append(result)
        return lst


rprint(Solution().runningSum, nums_lst)
