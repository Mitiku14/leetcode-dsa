class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            b = bin(i)
            ones = b[2:].count('1')
            res.append(ones)
        
        return res
        
