class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        
        return (first - 1) * (second - 1)