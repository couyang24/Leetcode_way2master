class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result += (ord(columnTitle[-i-1])-64)*26**i
        return result
