class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        half = total / 2
        heap = [-x for x in nums]
        heapq.heapify(heap)
        count = 0
        for x in nums:
            num = -heapq.heappop(heap)
            num /= 2
            total -= num
            count += 1
            if total <= half:
                return count
            heapq.heappush(heap, -num)
        
