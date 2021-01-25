class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        small = 0
        large = len(S)
        result = []
        for s in S:
            if s == "I":
                result.append(small)
                small += 1
            elif s == "D":
                result.append(large)
                large -= 1
        result.append(small)
        return result
