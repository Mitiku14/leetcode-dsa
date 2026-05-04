class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        seen = set()
        
        for r in range(row):
            for c in range(col):
                if (c, r) in seen:
                    continue
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                seen.add((r,c))
        for r in range(row):
            matrix[r].reverse()
        return matrix

        

