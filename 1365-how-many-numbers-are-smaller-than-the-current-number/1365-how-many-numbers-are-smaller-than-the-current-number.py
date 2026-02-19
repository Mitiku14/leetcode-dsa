class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num1 = sorted(nums)
        seen = {}
        for i, v in enumerate(num1):
            if v in seen:
                continue
            seen[v] = i
        res = []
        for num in nums:
            res.append(seen[num])

        return res