class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        l , r = 0, n - 1
        averages = []
        while l <= r:
            avg = (nums[l] + nums[r]) / 2
            averages.append(avg)
            l += 1
            r -= 1
        return min(averages)
        

