class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        modulo = 10**9 + 7
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                
                    if k < n and nums[i] == nums[j] * 2 and nums[k] == nums[j] * 2:
                        count += 1
        return count % modulo