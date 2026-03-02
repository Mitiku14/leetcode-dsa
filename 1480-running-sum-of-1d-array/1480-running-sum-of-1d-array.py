class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        res = []
        for i in range(1, n):
            prefix[i] =  prefix[i-1] + nums[i]
            res.append(prefix[i])
        return prefix
