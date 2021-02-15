class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        long = 0
        for i in range(len(s)):
            if s[i] in l:
                l=l[l.index(s[i])+1:]
                l.append(s[i])
            else:
                l.append(s[i])
            if len(l)>long:
                long = len(l)
        return long
