class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        ind = float('inf')
        num_ones = 0
        # count = 0
        flag = False
        for i in range(n):
            count = 0
            
            for j in range(m):
                print(mat[i][j])
                if mat[i][j] == 1:
                    flag = True
                    count += 1
                    
            if flag:
                if num_ones < count:
                    ind = i
                else:
                    
                    ind = min(ind, i)
                num_ones = max(num_ones, count)
        return [ind, num_ones] if flag else [0, 0]