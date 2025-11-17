class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count, l = 0, -1
        res = []
        for r in range(len(nums)):
            if nums[r] == 0:
                continue
            if l == -1:
                l = r 
                continue

            count = r - l -1
            l = r
        
            res.append(count)
        for num in res:
            if num < k:
                return False
        return True
