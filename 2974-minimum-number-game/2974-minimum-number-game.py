class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        res = []
        for x in nums:
            if not heap:
                return res
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            res.append(b)
            res.append(a)
        