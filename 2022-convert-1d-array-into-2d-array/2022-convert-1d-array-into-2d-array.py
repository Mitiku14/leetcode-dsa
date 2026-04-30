class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        new_mat = [[0] * n for _ in range(m)]
        if len(original) != m * n :
            return []
        for i in range(len(original)):
            new_mat[i //n][i % n] = original[i]
        return new_mat
            

