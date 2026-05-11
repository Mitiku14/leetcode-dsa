class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        n = len(nums)
        for i , num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
        selected = []
        for i in range(k):
            num, ind = heapq.heappop(heap)
            selected.append((-num, ind))
        selected.sort(key=lambda x: x[1])
        return [num for num, ind in selected]