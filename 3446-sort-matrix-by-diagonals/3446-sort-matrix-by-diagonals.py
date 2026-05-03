class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        n  = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                diagonals[i-j].append(grid[i][j])
        
        for key in diagonals:
            if key < 0:
                diagonals[key].sort()
            else:
                diagonals[key].sort(reverse=True)
        for i in range(n):
            for j in range(m):
                grid[i][j] = diagonals[i-j].pop(0)
        
        return grid