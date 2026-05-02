class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        # min_row = float('inf')
        row = []
        col = []
        max_col = 0
        for i in range(n):
            min_row = float('inf')
            for j in range(m):
                min_row = min(min_row, matrix[i][j])
            row.append(min_row)
        
        for j in range(m):
            max_row = 0
            for i in range(n):
                max_row = max(max_row, matrix[i][j])
            col.append(max_row)
        for num in row:
            if num in set(col):
                return [num]
        return []
            

        
