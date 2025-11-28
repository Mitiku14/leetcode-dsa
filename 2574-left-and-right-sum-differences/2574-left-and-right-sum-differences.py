class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixLeft = [0] * (n)
        prefixRight = [0] * (n)
        ReverseNums = nums[::-1]
        ans = [] 
        for i in range(1,n):
            prefixLeft[i] = prefixLeft[i - 1] + nums[i -1]
            prefixRight[i] = prefixRight[i - 1] + ReverseNums[i - 1]
        prefixRight = prefixRight[::-1]
        return [abs(prefixRight[i] - prefixLeft[i]) for i in range(len(prefixLeft))]
        



