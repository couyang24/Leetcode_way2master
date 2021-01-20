from helper import rprint2
from typing import Any, Dict, Iterable, List, Optional, Union

input1 = "ab"
input2 = "abc"
input3 = "cad"
lst1 = [input1, input2, input3]
sec_input1 = ["ad","bd","aaab","baa","badab"]
sec_input2 = ["a","b","c","ab","ac","bc","abc"]
sec_input3 = ["cc","acd","b","ba","bac","bad","ac","d"]
lst2 = [sec_input1, sec_input2, sec_input3]
output1 = 2
output2 = 7
output3 = 4
outputs = [output1, output2, output3,]

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            check = True
            for l in word:
                if l not in allowed:
                    check = False
            if check:
                count += 1
        return count

rprint2(Solution().countConsistentStrings, lst1, lst2, outputs)
