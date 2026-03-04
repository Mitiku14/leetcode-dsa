class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = {0: 1}
        cur = 0
        ans = 0
        for b in nums:
            cur += b
            temp = cur - goal
            ans += pref.get(temp, 0)
            pref[cur] = pref.get(cur, 0) + 1
        return ans
