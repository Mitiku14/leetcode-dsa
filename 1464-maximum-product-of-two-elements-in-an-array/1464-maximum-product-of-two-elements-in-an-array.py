class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                max_pro = max(max_pro, (nums[i] -1) * (nums[j] - 1))
        
        return max_pro