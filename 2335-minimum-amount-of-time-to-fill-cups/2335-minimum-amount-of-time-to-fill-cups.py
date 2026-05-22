class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = [-num for num in amount if num > 0]
        heapq.heapify(heap)
        time = 0
        while heap:
        
            if len(heap) >= 2:
            
                num1 = -heapq.heappop(heap)
                num2 = -heapq.heappop(heap)
                num1 -= 1
                num2 -= 1
                if num1 != 0:
                    heapq.heappush(heap, -num1) 
                if num2 != 0:
                    heapq.heappush(heap, -num2)
            else:
                num1 = -heapq.heappop(heap)
                num1 -= 1
                if num1 != 0:
                    heapq.heappush(heap, -num1)
        
            time += 1
        
        return time


        