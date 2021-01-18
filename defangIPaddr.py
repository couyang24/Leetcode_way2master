from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union

address1 = "1.1.1.1"
address2 = "255.100.50.0"
address_lst = [address1, address2]


class Solution:
    def defangIPaddr(self, address: str) -> str:
        addr_lst = address.split(".")
        return "[.]".join(addr_lst)

rprint(Solution().defangIPaddr, address_lst)
