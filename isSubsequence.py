class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = 0
        track = 0
        for l in s:
            for i in range(track, len(t)):
                print(l, t[i])
                if (l == t[i]):
                    check += 1
                    track = i+1
                    break
        return len(s) == check
