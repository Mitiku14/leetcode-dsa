class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = []
        n = len(nums)
        last = n - 1
        max_reach = 0
        for i in range(n):
            
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= last:
                return True
        
        
        return True