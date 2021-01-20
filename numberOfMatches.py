from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

input1 = 7
input2 = 14
inputs = [input1, input2]
output1 = 6
output2 = 13
outputs = [output1, output2]


class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            if n % 2 == 1:
                matches += (n - 1) / 2
                n = (n - 1) / 2 + 1
            else:
                matches += n / 2
                n = n / 2
        return int(matches)


rprint(Solution().numberOfMatches, inputs, outputs, mode="test")
