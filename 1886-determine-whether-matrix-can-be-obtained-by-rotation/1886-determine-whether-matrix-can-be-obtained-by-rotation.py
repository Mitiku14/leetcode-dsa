class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            n = len(mat)
            res = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    res[c][n-1-r] = mat[r][c]
            return res
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False

        

        
            

