from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union

input1 = "RLRRLLRLRL"
input2 = "RLLLLRRRLR"
input3 = "LLLLRRRR"
input4 = "RLRRRLLRLL"
inputs = [input1, input2, input3, input4]
output1 = 4
output2 = 3
output3 = 1
output4 = 2
outputs = [output1, output2, output3, output4]

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        bal = 0
        for index in range(len(s)):
            if bal == 0:
                count += 1
            if s[index] == "R":
                bal += 1
            else:
                bal -= 1
        return count

rprint(Solution().balancedStringSplit, inputs, outputs)
