
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []

        for i, num in enumerate(nums):
            heap.append((num, i))

        heapq.heapify(heap)
        for _ in range(k):
            value, idx = heapq.heappop(heap)

            new_value = value * multiplier
            nums[idx] = new_value

            heapq.heappush(heap, (new_value, idx))

        return nums