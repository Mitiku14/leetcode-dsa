class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.prefix = [[0] * (col + 1) for _ in range(row + 1)]
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                self.prefix[r][c] = self.prefix[r][c-1] + self.prefix[r-1][c] - self.prefix[r -1][c-1] + matrix[r-1][c-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 , c1 = row1 + 1, col1 + 1
        r2, c2 = row2  + 1, col2 + 1
        return (self.prefix[r2][c2] - self.prefix[r1 - 1][c2] - self.prefix[r2][c1 -1] + self.prefix[r1 -1][c1 -1])
        



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)