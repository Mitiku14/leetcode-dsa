class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        total_pairs = n * (n - 1) // 2
        good_pair = 0
        for i, num in enumerate(nums):

            
            pair = num - i
            print(num, i)
            # print(cnt[pair])

            good_pair += cnt[pair] 
            cnt[pair] += 1
        return total_pairs - good_pair

        