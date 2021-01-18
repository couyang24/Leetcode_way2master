# Leetcode: way 2 master

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## leetcode solutions:
I am currently working on putting all leetcode solutions in one place for people to use. I leveraged `termcolor` and `pyfiglet` to create clear separation for all the test examples and results. Please see input example and expected output below.

## Input Example:
```
from helper import rprint
from typing import Any, Dict, Iterable, List, Optional, Union

nums1 = [1,2,3,1,1,3]
nums2 = [1,1,1,1]
nums3 = [1,2,3]
nums_lst = [nums1, nums2, nums3]


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for index, num in enumerate(nums):
            if index == len(nums):
                pass
            else:
                for index2 in range(index+1, len(nums)):
                    if num == nums[index2]:
                        count += 1
        return count

rprint(Solution().numIdenticalPairs, nums_lst)
```

## Result Example:
```
_____                           _        _
| ____|_  ____ _ _ __ ___  _ __ | | ___  / |_
|  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \ | (_)
| |___ >  < (_| | | | | | | |_) | |  __/ | |_
|_____/_/\_\__,_|_| |_| |_| .__/|_|\___| |_(_)
                          |_|

********************************
The Input dataset is: [1, 2, 3, 1, 1, 3]
The Output dataset is: 4
********************************
 _____                           _        ____
| ____|_  ____ _ _ __ ___  _ __ | | ___  |___ \ _
|  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \   __) (_)
| |___ >  < (_| | | | | | | |_) | |  __/  / __/ _
|_____/_/\_\__,_|_| |_| |_| .__/|_|\___| |_____(_)
                          |_|

********************************
The Input dataset is: [1, 1, 1, 1]
The Output dataset is: 6
********************************
 _____                           _        _____
| ____|_  ____ _ _ __ ___  _ __ | | ___  |___ /_
|  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \   |_ (_)
| |___ >  < (_| | | | | | | |_) | |  __/  ___) |
|_____/_/\_\__,_|_| |_| |_| .__/|_|\___| |____(_)
                          |_|

********************************
The Input dataset is: [1, 2, 3]
The Output dataset is: 0
```

## Pull Request:
Feel free to PR unsolved questions or better solutions
