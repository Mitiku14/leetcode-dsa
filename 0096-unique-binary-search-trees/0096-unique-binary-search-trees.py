class Solution:
    def numTrees(self, n: int) -> int:
        prod = 1
        fact = 1
        for i in range(2 * n, 1, -1):
            prod *= i
        temp = 1
        for i in range(n, 0, -1):
            fact *= i
            temp *= (i + 1)
        return prod // ((temp) * fact)

        print(prod)