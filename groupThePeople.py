class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dct = {}
        result = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dct.keys():
                dct[groupSizes[i]] = [i]
            else:
                dct[groupSizes[i]].append(i)

        for i in dct:
            result.extend([dct[i][i*x:i*x+i] for x in range(int(len(dct[i])/i))])
        return result
