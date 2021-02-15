import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = itertools.permutations(nums)
        return [list(i) for i in perm]
