class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            l = 0
            n = len(nums)
            cur_sum = 0
            odd = 0
            count = 0
            for r in range(n):
                cur_sum += nums[r]
                if nums[r] %2 != 0:
                    odd += 1
                while odd > k:
                    if nums[l] %2 != 0:
                        odd -= 1
                    cur_sum -= nums[l]
                    l += 1
                count += (r - l + 1)
            return count
            
            
        return atmost(k) - atmost(k -1)


            

        
        