class Solution:
    def generateTheString(self, n: int) -> str:
        s = ""
        if n % 2 == 0:
            for i in range(n-1):
                s += "a"
            s += "b"
        else:
            for i in range(n):
                s += "a"
        return s
