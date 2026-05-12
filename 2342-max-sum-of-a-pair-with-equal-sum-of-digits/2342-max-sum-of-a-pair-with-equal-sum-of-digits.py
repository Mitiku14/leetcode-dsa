class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        for num in nums:
            digit = sum([int(d) for d in str(num)])
            cnt[digit].append(num)
        ans = -1
        for key, val in cnt.items():
            if len(val) < 2:
                continue
            val.sort(reverse=True)
            ans = max(ans, val[0] + val[1])
        return ans
            
