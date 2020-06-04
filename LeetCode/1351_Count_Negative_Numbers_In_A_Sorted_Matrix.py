class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        while len(grid) != 0:
            a = grid.pop()
            for i in a:
                if i < 0:
                    counter +=1
        return counter