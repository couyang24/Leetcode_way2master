class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        check = True
        for i in target:
            if target.count(i) != arr.count(i):
                check = False
        return check
