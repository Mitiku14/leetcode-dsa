class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        def stair(n):
            if n <= 2:
                return n
            if n not in self.memo:
                self.memo[n] = stair(n-1) + stair(n-2)
            return self.memo[n]
        return stair(n)
    
        