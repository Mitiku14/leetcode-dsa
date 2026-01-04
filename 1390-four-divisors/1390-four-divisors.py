from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        total = 0

        for x in nums:
            cnt = 0  
            s = 0    
            
            for d in range(1, x + 1):
                
                if x % d == 0:
                    cnt += 1   
                    s += d     

            
            if cnt == 4:
                total += s

        # Return final answer
        return total
