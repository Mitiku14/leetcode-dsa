class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                diagonals[i-j].append(mat[i][j])
        for key in diagonals:
            diagonals[key].sort()
        print(diagonals)
        for i in range(n):
            for j in range(m):
                mat[i][j] = diagonals[i-j].pop(0)
        
        return mat