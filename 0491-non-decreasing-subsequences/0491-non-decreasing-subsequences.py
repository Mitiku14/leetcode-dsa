class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(ind, cur):
            if len(cur) >= 2:
                res.append(cur.copy())
            used = set()
            for i in range(ind, n):
                if nums[i] in used:
                    continue
                if cur and nums[i] < cur[-1]:
                    continue
                used.add(nums[i])
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()
                
        backtrack(0, [])
        return res
