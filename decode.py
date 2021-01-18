from helper import rprint2
from typing import Any, Dict, Iterable, List, Optional, Union

encoded1 = [1,2,3]
encoded2 = [6,2,7,3]
lst1 = [encoded1, encoded2]
first1 = 1
first2 = 4
lst2 = [first1, first2]
output1 = [1,0,2,1]
output2 = [4,2,0,7,4]
outputs = [output1, output2]

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        lst = [first]
        for i in encoded:
            lst.append(lst[-1]^i)
        return lst

rprint2(Solution().decode, lst1, lst2, outputs)
