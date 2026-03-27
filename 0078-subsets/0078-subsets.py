class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        n = len(nums)
        def backtrack(i):
            if i == n:
                ans.append(sub[:])
                return 
            
            backtrack(i + 1)
            sub.append(nums[i])
            backtrack(i + 1)
            sub.pop()
        
        backtrack(0)
        return ans        