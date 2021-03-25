class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        m = 1
        while m < n:
            power += 1
            m = 2**power
        if m == n:
            return True
        else:
            return False
