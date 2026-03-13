class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if sorted(nums) == nums:
            return 0
        n = len(nums)
        limit = nums[n-1]
        count = 0
        for i in range(n-2, -1, -1):
            if nums[i] > limit:
                pieces = math.ceil(nums[i] / limit)
                count += pieces - 1
                limit = nums[i] // pieces
            else:
                limit = nums[i]

        return count
                    
