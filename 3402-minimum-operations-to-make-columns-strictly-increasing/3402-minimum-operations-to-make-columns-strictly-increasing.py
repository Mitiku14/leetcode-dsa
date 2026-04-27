class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        min_op = 0
        for j in range(m):
            prev = grid[0][j]
            for i in range(1,n):
                cur = grid[i][j]
                if prev >= cur:
                    min_op += (prev - cur + 1) 
                    grid[i][j] = prev + 1
                prev = grid[i][j]
        return min_op
         