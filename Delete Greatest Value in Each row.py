class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        row , column = len(grid) , len(grid[0])
        total = 0
        for i in range(row):
            grid[i].sort()

        for j in range(column):
            total += max(grid[i][j] for i in range(row))

        return total 
           
