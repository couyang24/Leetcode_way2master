class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for i in s.split():
            word = ""
            for j in range(1, len(i)+1):
                word += i[-j]
            result.append(word)
        return " ".join(result)
