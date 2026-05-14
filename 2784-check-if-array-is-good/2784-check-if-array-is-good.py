class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        summ = sum(nums)
        target = 0
        for i in range(1, m + 1):
            if i not in set(nums):
                return False
            target += i

        target += m
        if target != summ:
            return False
        return True
