class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_val = 0
        for i in range(n):
            for j in range(1, n):
                if colors[i] != colors[j]:
                    max_val = max(max_val, abs(i - j))
        
        return max_val
            
