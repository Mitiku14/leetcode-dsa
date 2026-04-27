class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return sum(cost)
        cost.sort(reverse=True)
        cnt = 1
        total = 0
        for i in range(n):
            if (i + 1) % 3 != 0:
                total += cost[i]
            else:
                continue
        return total