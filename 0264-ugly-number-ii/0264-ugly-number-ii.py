class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        
        sm = 1
        for _ in range(n):
            sm = heapq.heappop(heap)
            for num in [2, 3, 5]:
                new = num * sm
                if new not in seen:
                    heapq.heappush(heap, new)
                    seen.add(new)
        return sm
        

        

        

            

            