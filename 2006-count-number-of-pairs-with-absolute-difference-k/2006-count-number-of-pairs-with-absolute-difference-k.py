class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        count = 0
        for num in nums:
            count += cnt[num - k]
            count += cnt[num + k]
            cnt[num] += 1
        
        return count