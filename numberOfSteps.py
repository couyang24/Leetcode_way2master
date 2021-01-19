from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union
from icecream import ic

nums1 = 14
nums2 = 8
nums3 = 123
inputs = [nums1, nums2, nums3]
output1 = 6
output2 = 4
output3 = 12
outputs = [output1, output2, output3]

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num != 0:
            count += 1
            if num % 2 == 1:
                num -= 1
                if num == 0:
                    pass
                else:
                    count += 1
                    num /= 2
            else:
                num /= 2
                
        return count

rprint(Solution().numberOfSteps, inputs, outputs)
