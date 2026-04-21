class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        n = len(grid)
        m = len(grid[0])
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        def dfs( r, c):
            ans = 0
            if not inbound(r, c):
                return 1
            if grid[r][c] == 0:
                return 1
            if visited[r][c]:
                return 0
            visited[r][c] = True
            for nr, nc in dirs:
                ans += dfs(nr + r, nc + c)
            return ans
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs( i, j)

                    
    
        
                   

