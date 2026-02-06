class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = [k for k,_ in sorted_freq[:k]]
        return res


            