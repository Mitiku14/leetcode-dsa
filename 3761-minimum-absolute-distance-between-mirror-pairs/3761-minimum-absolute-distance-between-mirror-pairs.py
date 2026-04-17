class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = float('inf')
        for i , num in enumerate(nums):
            if num in  cnt:
                ans = min(ans, i - cnt[nums[i]])
            cnt[int(str(num)[::-1])] = i
        return ans if ans != float('inf') else - 1
        

