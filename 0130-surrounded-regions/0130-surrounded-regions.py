class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        n , m = len(board), len(board[0])
        if n <= 2 or m <= 2:
            return 
        q = deque()
        for r in range(n):
            q.append((r, 0))
            q.append((r, m - 1))
        for c in range(m):
            q.append((0, c))
            q.append((n-1, c))
        while q:
            r, c = q.popleft()
            if 0 <=r < n and 0 <= c < m and board[r][c] == "O":
                board[r][c] = "N"
                q.append((r, c + 1))
                q.append((r, c-1))
                q.append((r - 1, c))
                q.append((r +1, c))
            
        for r in range(n):
            for c in range(m):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"
                    