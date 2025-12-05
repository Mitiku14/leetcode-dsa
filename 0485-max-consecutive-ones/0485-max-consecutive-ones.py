class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_num = 0, 0
        n = len(nums) 
        for num in nums:
            if num == 1:
                count += 1
            else:
            
                count = 0 
            max_num = max(max_num, count) 
            
        return max_num