class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a_count = 0
        b_count = 0
        mid = int(len(s)/2) 
        a = s[:mid]
        b = s[mid:]
        for i in range(mid):
            if a[i] in vowels:
                a_count += 1
            if b[i] in vowels:
                b_count += 1
        return a_count == b_count
