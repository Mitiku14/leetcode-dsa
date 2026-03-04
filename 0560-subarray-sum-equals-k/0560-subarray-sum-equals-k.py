class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        count = 0
        cur = 0
        for num in nums:
            cur += num
            temp = cur - k
            count += prefix.get(temp , 0)
            prefix[cur] = prefix.get(cur, 0) + 1
        return count


        
              