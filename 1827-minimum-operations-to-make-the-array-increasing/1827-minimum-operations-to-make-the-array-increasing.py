class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                diff = nums[i-1] - nums[i]
                count += diff + 1
                nums[i] = nums[i-1]  + 1
        
        return count