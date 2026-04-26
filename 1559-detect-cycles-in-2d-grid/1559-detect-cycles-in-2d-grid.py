class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        visited = [[0] * m for _ in range(n)]

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(r, c, pr, pc):
            visited[r][c] = 1
            dirs = [(-1,0), (1,0), (0,1), (0,-1)]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if inbound(nr, nc):
                    if grid[r][c] == grid[nr][nc]:
                        if nr == pr and nc == pc:
                            continue
                        if visited[nr][nc]:
                            return True
                        if dfs(nr, nc, r, c):
                            return True

            return False

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True

        return False