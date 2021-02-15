class Solution:
    def minPartitions(self, n: str) -> int:
        max = 0
        for i in n:
            if int(i)>max:
                max = int(i)
        return max
