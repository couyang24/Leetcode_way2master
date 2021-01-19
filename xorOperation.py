from helper import rprint2
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

input1 = 5
input2 = 4
input3 = 1
lst1 = [input1, input2, input3]
sec_input1 = 0
sec_input2 = 3
sec_input3 = 7
lst2 = [sec_input1, sec_input2, sec_input3]
output1 = 8
output2 = 8
output3 = 7
outputs = [output1, output2, output3,]

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start
        for i in range(n-1):
            result = result ^ (start+2*(i+1))
        return result

rprint2(Solution().xorOperation, lst1, lst2, outputs, mode="test")
