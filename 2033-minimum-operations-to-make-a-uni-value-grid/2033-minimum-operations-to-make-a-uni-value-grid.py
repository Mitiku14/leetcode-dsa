class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            for val in row:
                arr.append(val)
        
        arr.sort()
        med = arr[len(arr) // 2]
        op = 0
        for val in arr:
            if (val - arr[0]) % x != 0:
                return -1
            op += abs(val - med) // x
        
        return op