from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

nums1 = 234
nums2 = 4421
inputs = [nums1, nums2]
output1 = 15
output2 = 21
outputs = [output1, output2]

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        n = str(n)
        for index in range(len(n)):
            product *= int(n[index])
            sum += int(n[index])
        return product - sum

rprint(Solution().subtractProductAndSum, inputs, outputs)
