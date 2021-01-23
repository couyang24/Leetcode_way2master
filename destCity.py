class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = paths[0][0]
        end = paths[0][1]
        index = []
        while end in [i[0] for i in paths]:
            start = end
            end = [i[1] for i in paths if i[0] == start][0]
        return end
