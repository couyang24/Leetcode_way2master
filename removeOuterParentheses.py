class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        result = ""
        for i, p in enumerate(S):
            pre_count = count
            if p == "(":
                count += 1
            elif p == ")":
                count -= 1
            if (i == 0) or (count == 0) or (pre_count == 0):
                continue
            else:
                result += p
        return result
