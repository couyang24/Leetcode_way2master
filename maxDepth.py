from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

input1 = "(1+(2*3)+((8)/4))+1"
input2 = "(1)+((2))+(((3)))"
input3 = "1+(2*3)/(2-1)"
input4 = "1"
inputs = [input1, input2, input3, input4]
output1 = 3
output2 = 3
output3 = 1
output4 = 0
outputs = [output1, output2, output3, output4]

class Solution:
    def maxDepth(self, s: str) -> int:
        track = 0
        max = 0
        for l in s:
            if l == "(":
                track += 1
                if track > max:
                    max = track
            elif l == ")":
                track -= 1
        return max

rprint(Solution().maxDepth, inputs, outputs, mode="test")
