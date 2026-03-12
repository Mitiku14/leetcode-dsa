class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_inc = deque()
        min_dec = deque()
        l = 0
        max_len = 0

        for r in range(len(nums)):
            while max_inc and nums[r] < max_inc[-1]:
                max_inc.pop()
            max_inc.append(nums[r])

            while min_dec and nums[r] > min_dec[-1]:
                min_dec.pop()
            min_dec.append(nums[r])

            while abs(max_inc[0] - min_dec[0]) > limit:
                if nums[l] == max_inc[0]:
                    max_inc.popleft()

                if nums[l] == min_dec[0]:
                    min_dec.popleft()
                
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len

    
        


