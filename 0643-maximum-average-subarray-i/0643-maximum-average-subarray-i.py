class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        l, avg = 0, float("-inf")
        total = 0
        for r in range(n):
            total += nums[r]
            if  (r - l + 1) == k:
                avg = max(avg, total/k)
                total -= nums[l]
                l += 1
        return avg

