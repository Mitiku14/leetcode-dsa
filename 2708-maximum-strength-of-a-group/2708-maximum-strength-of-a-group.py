class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        max_pro = float('-inf')
        n = len(nums)
        def backtrack(ind, group):
            nonlocal max_pro
            if group != float('-inf'):
                max_pro = max(max_pro, group)
            if ind >= n:
                return 
            # for i in range(ind + 1, len(group)):
                
            #     cur = 1
            #     cur *= group[i]
            #     max_pro = max(max_pro, cur)
            backtrack(ind + 1, group * nums[ind] if group != float('-inf') else nums[ind])
            backtrack(ind + 1, group)

            
        backtrack(0, float('-inf'))
        return max_pro



            