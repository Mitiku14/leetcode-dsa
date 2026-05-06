from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])

        # Step 1: rotate (transpose + reverse rows)
        rotated = [[None] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                rotated[j][n - 1 - i] = boxGrid[i][j]
        for col in range(n):  
            empty = m - 1 

            for row in range(m - 1, -1, -1):
                if rotated[row][col] == '*':
                    empty = row - 1  
                elif rotated[row][col] == '#':
                    rotated[row][col] = '.'
                    rotated[empty][col] = '#'
                    empty -= 1

        return rotated