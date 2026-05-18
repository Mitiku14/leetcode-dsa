class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        cap_pro = [(c, p) for c, p in zip(capital, profits)]
        cap_pro.sort()
        i = 0
        ans = 0

        for op in range(k):
            while i < len(profits) and cap_pro[i][0] <= w:
                heappush(heap, -cap_pro[i][1])
                i += 1
            if not heap:
                break
            w -= heapq.heappop(heap)
            # k -= 1
        return w

