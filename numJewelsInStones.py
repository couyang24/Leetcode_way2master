from helper import rprint2
from typing import Any, Dict, Iterable, List, Optional, Union

J1 = "aA"
J2 = "z"
lst1 = [J1, J2]
S1 = "aAAbbbb"
S2 = "ZZ"
lst2 = [S1, S2]


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in J:
            for j in S:
                if i == j:
                    count += 1
        return count


rprint2(Solution().numJewelsInStones, lst1, lst2)
