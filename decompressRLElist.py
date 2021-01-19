from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

nums1 = [1,2,3,4]
nums2 = [1,1,2,3]
inputs = [nums1, nums2]
output1 = [2,4,4,4]
output2 = [1,3,3]
outputs = [output1, output2]

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst = []
        for index in range(int((len(nums)+1)/2)):
            for count in range(nums[index*2]):
                lst.append(nums[index*2+1])
        return lst

rprint(Solution().decompressRLElist, inputs, outputs)
