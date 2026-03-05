class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        min_val = 0
        pref = [0] * (n)
        pref[0] = nums[0]
        for i in range(1,n):
            pref[i] = pref[i-1] + nums[i]
        for i in range(n):
            min_val = min(min_val, pref[i])
        return 1- min_val

        
