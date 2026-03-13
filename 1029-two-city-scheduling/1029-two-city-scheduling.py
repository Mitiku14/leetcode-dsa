class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        sorted_costs = sorted(costs, reverse=True)
        ans = []
        i = 0
        for x, y in costs:
            ans.append((x-y, i))
            i += 1

        ans.sort()
        res = 0
        j = 0
        for _, ind in ans:
            if j < n//2:
                res += costs[ind][0]
            else:
                res += costs[ind][1]
            j += 1
        
        return res