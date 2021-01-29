class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for i in range(len(A[0])):
            check = True
            pre = "a"
            for j in A:
                if ord(j[i]) < ord(pre):
                    check = False
                pre = j[i]
            if check == True:
                count += 1
        return len(A[0]) - count
