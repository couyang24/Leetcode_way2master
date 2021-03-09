class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber>=1:
            if columnNumber%26==0:
                result = "Z" + result
                if columnNumber==26:
                    columnNumber = 0
                columnNumber //= 26
                columnNumber -= 1
            else:
                result = chr(columnNumber%26+64) + result
                columnNumber //= 26
        return result
