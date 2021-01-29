class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        dct = {1:0, 2:0}
        for i in position:
            if i%2 == 0:
                dct[2] += 1
            else:
                dct[1] += 1
        return min(dct[2], dct[1])
