class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        start = image[sr][sc]
        dirs = [(-1, 0),  (1, 0), (0, -1), (0, 1)]
        visited = [[False] * m for _ in range(n)]
        image[sr][sc] = color
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        def dfs(r, c):
            visited[r][c] = True
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not inbound(nr, nc) or visited[nr][nc]:
                    continue
                if image[nr][nc] == start:
                    image[nr][nc] = color
                    dfs(nr, nc)
                visited[nr][nc] = True
        
        dfs(sr, sc)
        return image
                

        