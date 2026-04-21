class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(r, c):
            if not inbound(r, c) or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count