class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        res = []
        for i in range(n):
            if i % 2 == 0:
                for j in range(m):
                    if ( i + j) % 2 == 0:
                        res.append(grid[i][j])
            else:
                for j in range(m -1, -1, -1):
                    if (i +j) % 2 == 0:
                        res.append(grid[i][j])
        return res