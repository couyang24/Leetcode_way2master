from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

input1 = [1,4,2,5,3]
input2 = [1,2]
input3 = [10,11,12]
inputs = [input1, input2, input3]
output1 = 58
output2 = 3
output3 = 66
outputs = [output1, output2, output3]


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(int((len(arr)+1)/2)):
            for j in range(len(arr)-i*2):
                result += sum(arr[j:(j+i*2+1)])
        return result

rprint(Solution().sumOddLengthSubarrays, inputs, outputs, mode="test")
