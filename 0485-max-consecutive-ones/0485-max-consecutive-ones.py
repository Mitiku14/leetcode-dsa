class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
            max_con = max(max_con, r - l + 1)
        return max_con