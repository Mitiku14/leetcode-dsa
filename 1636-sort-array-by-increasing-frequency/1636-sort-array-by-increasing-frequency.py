class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        sorted_nums = sorted(freq.items(), key=lambda x: (x[1], -x[0]))
        print(sorted_nums)
        ans = []
        for key, val in sorted_nums:
            res = [key] * val
            ans.extend(res)
        return ans
