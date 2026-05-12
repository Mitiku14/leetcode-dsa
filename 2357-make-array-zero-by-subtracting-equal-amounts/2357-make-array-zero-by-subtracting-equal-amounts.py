class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num = list(set(nums))
        n = len(num)
        cnt = 0
        for x in num:
            if x == 0:
                cnt += 1
        
        return n - cnt