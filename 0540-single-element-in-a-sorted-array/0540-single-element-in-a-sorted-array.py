class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for key, val in cnt.items():
            if val == 1:
                return key
        