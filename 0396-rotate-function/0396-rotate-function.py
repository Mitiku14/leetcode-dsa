class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        
        F = 0
        for i in range(n):
            F += i * nums[i]
        
        res = F
        
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            res = max(res, F)
        
        return res