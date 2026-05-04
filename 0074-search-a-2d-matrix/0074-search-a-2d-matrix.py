class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            arr = matrix[i]
            l , r = 0, len(arr) -1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return True
                elif arr[m] > target:
                    r -= 1
                else:
                    l += 1
        return False

        
        # def check(arr):
        #     if arr[-1] > 
        #     size = len(arr)
        #     l , r = 0, size - 1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if arr[mid] == target:
        #             return True
        #         elif arr[mid] <
        
    
        