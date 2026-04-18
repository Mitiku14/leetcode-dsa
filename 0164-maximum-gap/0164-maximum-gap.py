class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_diff = 0
        n = len(nums)
        for i in range(n-1):
            max_diff = max(max_diff, abs(nums[i] - nums[i + 1]))
        return max_diff

        