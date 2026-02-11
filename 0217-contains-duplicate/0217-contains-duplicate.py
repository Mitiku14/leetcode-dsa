class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        res = []
        for key, val in cnt.items():
            if val >= 2:
                return True
        return False

