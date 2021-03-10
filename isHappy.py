class Solution:
    def isHappy(self, n: int) -> bool:
        memory = []
        while n not in memory:
            memory.append(n)
            result = 0
            for i in str(n):
                result += int(i)**2
            n = result
        if n == 1:
            return True
        else:
            return False
