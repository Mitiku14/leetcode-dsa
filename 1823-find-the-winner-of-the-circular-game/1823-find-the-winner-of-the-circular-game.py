class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
    
        def findWinner(n):
            if n == 1:
                return 0
            
            return (findWinner(n-1) + k) % n
        
        return findWinner(n) + 1