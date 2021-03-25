class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        check = True
        while check == True:
            check = False
            if n%2 == 0:
                check = True
                n /= 2
            elif n%3 == 0:
                check = True
                n /= 3
            elif n%5 == 0:
                check = True
                n /= 5
        
        if n == 1:
            return True
        else:
            return False
