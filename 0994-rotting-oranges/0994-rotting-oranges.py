class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        q = deque()
        fresh , time = 0, 0
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for nr, nc in dirs:
                    new_row = nr + r
                    new_col = nc + c
                    if not inbound(new_row, new_col) or grid[new_row][new_col] != 1:
                        continue
                    grid[new_row][new_col] = 2
                    q.append([new_row, new_col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1


                


        