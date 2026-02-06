class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt_duplicates = Counter(nums)
        res = []
        for key, val in cnt_duplicates.items():
            if val == 2:
                res.append(key)
        return res
