class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            temp = sum(int(x) for x in str(num))
            res.append(temp)
        return min(res)
        