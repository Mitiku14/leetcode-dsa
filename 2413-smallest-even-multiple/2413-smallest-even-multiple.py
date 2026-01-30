class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res = n * 2
        if n % 2 == 0:
            return n
        else:
            return res