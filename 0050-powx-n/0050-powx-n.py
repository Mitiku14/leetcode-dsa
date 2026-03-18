class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculatePow(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            
            elif exponent % 2 == 0:
                return calculatePow(base * base, exponent // 2)
            else:
                return base * calculatePow(base * base, (exponent -1) // 2)
        
        res = calculatePow()
        return float(res) if n >= 0 else 1 / res

        
        