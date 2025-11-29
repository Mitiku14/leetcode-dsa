class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = {0:-1}
        totalSum = 0
        for i, num in enumerate(nums):
            totalSum += num

            if k != 0:
                totalSum %= k
            if totalSum in prefix_mod:
                if i - prefix_mod[totalSum] > 1:
                    return True
            else:
                prefix_mod[totalSum] = i
        
        return False
        