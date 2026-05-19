class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def backtrack(i):
            if i >= len(nums): return 0
            if i not in memo:
                temp = backtrack(i + 1)
                mine = nums[i]
                memo[i] = max(temp, mine + backtrack(i + 2))
            return memo[i]
        return backtrack(0)

        