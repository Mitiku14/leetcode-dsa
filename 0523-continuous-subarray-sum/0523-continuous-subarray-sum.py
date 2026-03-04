class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0: -1}
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            if k != 0:
                cur_sum %= k
            if cur_sum in prefix:
                if i - prefix[cur_sum] > 1:
                    print(cur_sum)
                    return True
            else:
                prefix[cur_sum] = i
        

        return False
        



        