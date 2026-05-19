class Solution:
    def fib(self, n: int) -> int:
        self.memo = {}
        def f(num):
            if num < 2:
                return num
            if num not in self.memo:
                self.memo[num] = f(num-2) + f(num-1)
            
            return self.memo[num]
        
        return f(n)
