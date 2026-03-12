class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n -2):
            if nums[i] == 0:
                nums[i] = nums[i] ^ 1
                nums[i + 1] = nums[i + 1] ^ 1
                nums[i + 2] = nums[i + 2] ^ 1
                count += 1
        
        if all(num == 1 for num in nums):
            return count
        return -1