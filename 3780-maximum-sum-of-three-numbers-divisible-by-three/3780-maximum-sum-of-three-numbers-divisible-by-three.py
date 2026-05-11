class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        if len(nums) == 3 and sum(nums) % 3:
            return 0

        possible = defaultdict(list)
        for num in nums:
            possible[num % 3].append(num)
        ans = 0
        for r in possible:
            possible[r].sort(reverse=True)
        
        if len(possible[0]) >= 3:
            ans = max(ans, sum(possible[0][:3]))      
        if len(possible[1]) >= 3:
            ans = max(ans, sum(possible[1][:3]))
        if len(possible[2]) >= 3:
            ans = max(ans, sum(possible[2][:3]))
        if possible[0] and possible[1] and possible[2]:
            ans = max(ans, possible[0][0] + possible[1][0] + possible[2][0])
        
        return ans 

        
