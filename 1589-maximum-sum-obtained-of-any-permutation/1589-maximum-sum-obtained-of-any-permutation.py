class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        modulo = 10**9 + 7
        diff = [0] * (n + 1)
        for x, y in requests:
            diff[x] += 1
            diff[y + 1] -= 1

        pref = [0] * n
        pref[0] = diff[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + diff[i]
        pref.sort()
        nums.sort()
        ans = 0
        for i in range(n):
            ans += pref[i] * nums[i]
        return ans % modulo
