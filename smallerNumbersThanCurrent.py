from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union

nums1 = [8,1,2,2,3]
nums2 = [6,5,4,8]
nums3 = [7,7,7,7]
inputs = [nums1, nums2, nums3]
output1 = [4,0,1,1,3]
output2 = [2,1,0,3]
output3 = [0,0,0,0]
outputs = [output1, output2, output3]

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            lst.append(count)
        return lst


rprint(Solution().smallerNumbersThanCurrent, inputs, outputs)
