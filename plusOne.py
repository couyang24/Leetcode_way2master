class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = [str(i) for i in digits]
        return [int(i) for i in str(int("".join(string))+1)]
