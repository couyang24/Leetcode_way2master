class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            result = "-"
            for i in range(1, len(str(x))):
                result += str(x)[-i]
        else:
            result = ""
            for i in range(1, len(str(x))+1):
                result += str(x)[-i]
        if (int(result)>2**31-1) or (int(result)<-2**31):
            return 0
        else:
            return int(result)
