class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for row in grid:
            row.sort()
        res = 0
        for c in range(m-1, -1, -1):
            max_val = 0
            for r in range(n):
                max_val = max(max_val, grid[r][c])
            res += max_val
        
        return res
            



