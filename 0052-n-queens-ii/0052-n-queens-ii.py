class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [[0] * n for _ in range(n)]
        
        cols = set()
        diag1 = set() 
        diag2 = set()   
        
        def backtrack(row):
            nonlocal res
            if row == n:
                res += 1
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                board[row][col] = 1
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                backtrack(row + 1)
            
                board[row][col] = 0
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        backtrack(0)
        return res
