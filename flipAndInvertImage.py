from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

nums1 = [[1,1,0],[1,0,1],[0,0,0]]
nums2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
inputs = [nums1, nums2]
output1 = [[1,0,0],[0,1,0],[1,1,1]]
output2 = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
outputs = [output1, output2]


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for l in A:
            lst = []
            for index in range(len(l)):
                lst.append(1 - l[len(l)-index-1])
            result.append(lst)
        return result


rprint(Solution().flipAndInvertImage, inputs, outputs, mode="test")
