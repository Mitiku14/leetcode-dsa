class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m        
        def dfs(r, c):
            if not inbound(r, c) or grid[r][c] == 0:
                return 0
            total = grid[r][c]
            grid[r][c] = 0
            for dr, dc in dirs:
                nr , nc = r + dr, c + dc
                total += dfs(nr, nc)
            return total
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    val = dfs(i, j)
                    if val % k == 0:
                        count += 1
        return count