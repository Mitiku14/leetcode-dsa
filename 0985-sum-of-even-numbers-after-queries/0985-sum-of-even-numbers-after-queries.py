class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for val, ind in queries:
            nums[ind] = nums[ind] + val
            even_sum = sum([x for x in nums if x % 2 == 0])
            res.append(even_sum)
        return res