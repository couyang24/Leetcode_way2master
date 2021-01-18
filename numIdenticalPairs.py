from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union

nums1 = [1,2,3,1,1,3]
nums2 = [1,1,1,1]
nums3 = [1,2,3]
nums_lst = [nums1, nums2, nums3]


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for index, num in enumerate(nums):
            if index == len(nums):
                pass
            else:
                for index2 in range(index+1, len(nums)):
                    if num == nums[index2]:
                        count += 1
        return count

rprint(Solution().numIdenticalPairs, nums_lst)
