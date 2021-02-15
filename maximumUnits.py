class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total = 0
        sorted_list = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        for i in sorted_list:
            if truckSize != 0:
                if i[0] < truckSize:
                    truckSize -= i[0]
                    total += i[0]*i[1]
                else:
                    total += truckSize*i[1]
                    truckSize = 0
        return total
