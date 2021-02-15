class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        orig = sum([sum(l) for l in grid])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = min(max(grid[i]), max([h[j] for h in grid]))
        return sum([sum(l) for l in grid]) - orig
