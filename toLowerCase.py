class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ""
        for i in str:
            result += i.lower()
        return result
