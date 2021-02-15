class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct = {}
        for i in arr:
            if i in dct.keys():
                dct[i] += 1
            else:
                dct[i] = 1
        if len(dct.values()) == len(set(dct.values())):
            return True
        else:
            return False
