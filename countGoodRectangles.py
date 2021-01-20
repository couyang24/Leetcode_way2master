class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max = 0
        for r in rectangles:
            if min(r) > max:
                count = 1
                max = min(r)
            elif min(r) == max:
                count += 1
        return count
