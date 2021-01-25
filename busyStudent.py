class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in list(map(list, zip(startTime, endTime))):
            for j in range(i[0], i[1]+1):
                if j == queryTime:
                    count += 1
        return count
