class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(nums, k):
            count_good = 0
            l = 0
            res = []
            freq = defaultdict(int)
            for r in range(len(nums)):
                freq[nums[r]] += 1
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                count_good += r - l + 1
            return count_good
        return at_most(nums,k) - at_most(nums, k- 1)

        