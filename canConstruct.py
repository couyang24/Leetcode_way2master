class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = True
        for l in ransomNote:
            if l not in magazine:
                check = False
            else:
                magazine = magazine[:magazine.find(l)]+magazine[magazine.find(l)+1:]
        return check
