class Solution:
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])
        start = image[sr][sc]
        if start == color:
            return image

        dirs = [
            (-1, 0),  
            (1, 0),   
            (0, -1),  
            (0, 1)    
        ]

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols
        q = deque()
        q.append((sr, sc))
        image[sr][sc] = color
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr , nc = r + dr, c + dc
                if inbound(nr, nc ) and image[nr][nc] == start:
                    image[nr][nc] = color
                    q.append((nr, nc))
        
        return image

                
            