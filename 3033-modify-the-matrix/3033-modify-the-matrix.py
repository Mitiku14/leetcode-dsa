class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        def check(col):
            max_val = 0
            for i in range(n):
                max_val = max(max_val, matrix[i][col])
            return max_val

        for i in range(n):       
            for j in range(m):    
                if matrix[i][j] == -1:
                    y = check(j)  
                    matrix[i][j] = y

        return matrix