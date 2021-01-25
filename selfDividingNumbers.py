class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        result = []

        for i in range(left, right + 1):
            check = True
            for d in str(i):
                if d == "0":
                    check = False
                    pass
                elif i % int(d) != 0:
                    check = False

            if check:
                result.append(i)

        return result
