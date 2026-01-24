class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        max_pair_sum = 0
        while l <= r:
            total = nums[l] + nums[r]
            max_pair_sum = max(max_pair_sum, total)
            l += 1
            r -= 1
        return max_pair_sum


