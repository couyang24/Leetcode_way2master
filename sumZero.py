class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n%2 == 0:
            for i in range(1, int(n/2+1)):
                result.append(i)
                result.append(-i)
        else:
            for i in range(1, int((n+1)/2)):
                result.append(i)
                result.append(-i)
            result.append(0)
            
        return result
