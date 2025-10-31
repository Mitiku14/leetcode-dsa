class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            y = nums[i-1]
            if nums[i] == y:
                return nums[i]
                break
                