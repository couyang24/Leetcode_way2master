class Solution:
    def maximum69Number (self, num: int) -> int:
        string = str(num)
        change = True
        result = ""
        for i, l in enumerate(string):
            if (l == "6") & change:
                result += "9"
                change = False
            else:
                result += l
        return result
