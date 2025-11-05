class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        MOD = 10**9 + 7
        ans = []
        for i in range(n):
            res = 0
            r = i
            # keep extending r from i to n-1
            while r < n:
                res += nums[r]
                ans.append(res)
                r += 1

        ans.sort()
        return sum(ans[left-1:right]) % MOD
        




                        
