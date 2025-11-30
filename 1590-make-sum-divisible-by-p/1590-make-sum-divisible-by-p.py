class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums)
        rem = total % p
        if rem == 0:
            return 0
        prefix_ind = {0: -1}
        prefix = 0
        ans = n
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            modValue = (prefix - rem + p) % p
            if modValue in prefix_ind:
                ans = min(ans, i - prefix_ind[modValue])
            
            prefix_ind[prefix] = i

        return ans if ans < n else -1

        