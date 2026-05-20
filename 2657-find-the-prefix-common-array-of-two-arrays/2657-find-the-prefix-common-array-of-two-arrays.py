class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        seen = [0] * (n + 1)
        cnt = 0
        for i in range(n):
            seen[A[i]] += 1
            if seen[A[i]] == 2:
                cnt += 1
            
            seen[B[i]] += 1
            if seen[B[i]] == 2:
                cnt += 1
            
            res[i] = cnt
        return res

