class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        cur_sum = 0
        count = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            diff = cur_sum % k
            count += freq.get(diff, 0)
            freq[diff] = freq.get(diff , 0) + 1
        return count
        
    