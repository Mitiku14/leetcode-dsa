class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        small = arrays[0][0]
        big = arrays[0][-1]

        max_dist = 0
        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_dist = max(max_dist, abs(arr[-1] - small), abs(big - arr[0]))
            small = min(small, arr[0])
            big = max(big, arr[-1])
        
        return max_dist
        