class Solution:
    def isPalindrome(self, x: int) -> bool:
        check = True
        for i in range(len(str(x))):
            if str(x)[i] != str(x)[-i-1]:
                check = False
        return check
