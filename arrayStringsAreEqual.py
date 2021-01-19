from helper import rprint2
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

input1 = ["ab", "c"]
input2 = ["a", "cb"]
input3 = ["abc", "d", "defg"]
lst1 = [input1, input2, input3]
sec_input1 = ["a", "bc"]
sec_input2 = ["ab", "c"]
sec_input3 = ["abcddefg"]
lst2 = [sec_input1, sec_input2, sec_input3]
output1 = True
output2 = False
output3 = True
outputs = [output1, output2, output3,]

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

rprint2(Solution().arrayStringsAreEqual, lst1, lst2, outputs, mode="test")
