class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dist = list(set(nums))
        heap = []
        if len(dist) <= 2:
            return max(dist)
        for num in dist:
            heapq.heappush(heap, num)
            if len(heap) > 3:
                heapq.heappop(heap)
        
        return heap[0]