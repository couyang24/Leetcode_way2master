from helper import rprint2
from typing import Any, Dict, Iterable, List, Optional, Union

nums1 = [0,1,2,3,4]
nums2 = [1,2,3,4,0]
nums3 = [1]
inputs1 = [nums1, nums2, nums3]
index1 = [0,1,2,2,1]
index2 = [0,1,2,3,0]
index3 = [0]
inputs2 = [index1, index2, index3]
output1 = [0,4,1,3,2]
output2 = [0,1,2,3,4]
output3 = [1]
outputs = [output1, output2, output3]

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        lst = []
        for i in range(len(index)):
            lst.insert(index[i], nums[i])
        return lst

rprint2(Solution().createTargetArray, inputs1, inputs2, outputs)
