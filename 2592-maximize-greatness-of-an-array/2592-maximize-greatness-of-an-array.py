class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = j = 0
        count = 0
        while j < n:
            if nums[i] < nums[j]:
                count += 1
                i += 1
            j += 1
        return count
