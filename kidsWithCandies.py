from helper import sprint
from typing import Any, Dict, Iterable, List, Optional, Union

candies1 = [2, 3, 5, 1, 3]
candies2 = [4, 2, 1, 1, 2]
candies3 = [12, 1, 12]
candies_lst = [candies1, candies2, candies3]
extraCandies1 = 3
extraCandies2 = 1
extraCandies3 = 10
extraCandies_lst = [extraCandies1, extraCandies2, extraCandies3]


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        max = 0
        for num in candies:
            if num > max:
                max = num

        for num in candies:
            lst.append(num + extraCandies >= max)

        return lst


for index, candies in enumerate(candies_lst):
    result_lst = Solution().kidsWithCandies(candies, extraCandies_lst[index])
    sprint("Example {}:".format(index + 1))
    print("********************************")
    print("The Input dataset is: {}".format(candies))
    print("The Output dataset is: {}".format(result_lst))
    print("********************************")
