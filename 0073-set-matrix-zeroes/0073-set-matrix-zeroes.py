class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row1 = set()
        col1 =set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row1.add(i)
                    col1.add(j)
        for r in range(row):
            for j in range(col):
                if r in row1 or j in col1:
                    matrix[r][j] = 0
        return matrix





                    
        
        