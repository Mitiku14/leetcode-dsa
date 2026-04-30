class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        flag = False
        for i in range(n-1):
            white = 0
            black = 0
            for j in range(m - 1):
                a = grid[i][j]
                b = grid[i + 1][j]
                c = grid[i][j + 1]
                d = grid[i + 1][j + 1]
                cells = [a , b, c , d]
                white = cells.count('W')
                black = cells.count('B')
                if white != black:
                    flag = True
        if flag:
            return True
        return False
        

                
                