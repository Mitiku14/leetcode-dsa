class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = []
        n = len(nums)
        for key,val in cnt.items():
            if val == 2:
                res.append(key)
        seen = set(nums)
        for i in range(1, n + 1):
            if i not in seen:
                res.append(i)
                break
        return res
        