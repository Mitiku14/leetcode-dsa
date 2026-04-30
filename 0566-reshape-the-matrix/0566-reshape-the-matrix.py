class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat[0])
        m = len(mat)
        shaped = [[0] * c for _ in range(r)]
        if r * c != m * n:
            return mat
        cnt = 0
        for i in range(m):
            for j in range(n):
                shaped[cnt//c][cnt % c] = mat[i][j]
                cnt += 1
        return shaped
        





        
        
        
