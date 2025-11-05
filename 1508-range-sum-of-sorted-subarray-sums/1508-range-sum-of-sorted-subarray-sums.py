class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        res = 0
        ans = []
        for i in range(len(nums)):
            res = nums[i]
            ans.append(res)
            for j in range(i + 1, len(nums)):
                res += nums[j]
                ans.append(res)
        ans.sort()
        # print(ans)
        return sum(ans[left -1 : right]) % mod
        




                        
