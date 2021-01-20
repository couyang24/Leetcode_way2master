class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        for i, l in enumerate(mat):
            if (i == (len(l)-1)/2):
                count += l[i]
            else:
                count += l[i]+l[-1-i]
        return count
