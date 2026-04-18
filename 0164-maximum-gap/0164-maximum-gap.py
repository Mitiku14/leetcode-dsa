class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) < 2:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        bucket_size = len(nums)
        bucket_count = (max_val - min_val) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]
        for num in nums:
            ind = (num - min_val) // bucket_size
            buckets[ind].append(num) 
        res = [] 
        for bucket in buckets:
            bucket.sort()
            res.extend(bucket)
        max_diff = 0
        for i in range(n -1):
            max_diff = max(max_diff, abs(res[i] - res[i + 1]))
        
        return max_diff

