from helper import sprint
from typing import Any, Dict, Iterable, List, Optional, Union

nums1 = [2,5,1,3,4,7]
nums2 = [1,2,3,4,4,3,2,1]
nums3 = [1,1,2,2]
nums_lst = [nums1, nums2, nums3]
n1 = 3
n2 = 4
n3 = 2
n_lst = [n1, n2, n3]


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst = []
        if len(nums) == 2:
            return nums
        else:
            multi = int((len(nums)+1)/n)
            for i in range(n):
                for cyc in range(multi):
                    lst.append(nums[n*cyc+i])
            return lst

for index, nums in enumerate(nums_lst):
    result_lst = Solution().shuffle(nums, n_lst[index])
    sprint("Example {}:".format(index + 1))
    print("********************************")
    print("The Input dataset is: {} & {}".format(nums, n_lst[index]))
    print("The Output dataset is: {}".format(result_lst))
    print("********************************")
