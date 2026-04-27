from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        mapp = {
            1: [0, 2],   # right, left
            2: [1, 3],   # down, up
            3: [2, 1],   # left, down
            4: [0, 1],   # right, down
            5: [2, 3],   # left, up
            6: [0, 3]    # right, up
        }

        # right, down, left, up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # FIX: dimensions should be n x m
        visited = [[False] * m for _ in range(n)]

        opposite = {
            0: 2,   # right -> left
            1: 3,   # down -> up
            2: 0,   # left -> right
            3: 1    # up -> down
        }

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        q = deque([(0, 0)])
        visited[0][0] = True

        while q:
            r, c = q.popleft()
            if r == n - 1 and c == m - 1:
                return True

            for d in mapp[grid[r][c]]:
                nr = r + dirs[d][0]
                nc = c + dirs[d][1]

                if not inbound(nr, nc):
                    continue

                if visited[nr][nc]:
                    continue

                next_type = grid[nr][nc]

                if opposite[d] in mapp[next_type]:
                    visited[nr][nc] = True
                    q.append((nr, nc))

        return False