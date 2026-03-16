class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        temp = 1
        i = 0
        count = 0
        while temp <= n:
            if i < len(nums) and nums[i] <= temp:
                temp += nums[i]
                i += 1
            else:
                temp += temp
                count += 1
        return count


        
