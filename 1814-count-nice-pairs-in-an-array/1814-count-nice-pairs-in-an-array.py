class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        count = 0
        mod = 10 **9 + 7
        for num in nums:
            temp = num - int(str(num)[::-1])
            count += cnt[temp]
            cnt[temp] += 1
        return count % mod
