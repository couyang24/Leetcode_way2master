om helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union

accounts1 = [[1,2,3],[3,2,1]]
accounts2 = [[1,5],[7,3],[3,5]]
accounts3 = [[2,8,7],[7,1,3],[1,9,5]]
accounts_lst = [accounts1, accounts2, accounts3]


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for acct in accounts:
            wealth = 0
            for money in acct:
                wealth += money
            if wealth > max:
                max = wealth
        return max

rprint(Solution().maximumWealth, accounts_lst)
