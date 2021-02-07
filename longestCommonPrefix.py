class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if strs == []:
            return prefix
        for j in range(min([len(i) for i in strs])):
            bench = strs[0][j]
            for k in strs:
                if k[j] != bench:
                    return prefix
            prefix += bench
        return prefix
                
