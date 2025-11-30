class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = []
        for num in cnt:
            if cnt[num] > 1:
                res.append(num)


        return res