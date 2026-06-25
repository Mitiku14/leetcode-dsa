class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        cnt_target = 0
        
        if target not in set(nums):
            return 0
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(i,  n):
                if nums[j] == target:
                    cnt += 1
                length = j - i + 1
                if cnt > length // 2:
                    cnt_target += 1
            
        return cnt_target





