class Solution:
    def judgeCircle(self, moves: str) -> bool:
        lat = 0
        lng = 0
        for move in moves:
            if move == "U":
                lat += 1
            elif move == "D":
                lat -= 1
            elif move == "L":
                lng -= 1
            elif move == "R":
                lng += 1
        if (lat == 0) & (lng == 0):
            return True
        else:
            return False
