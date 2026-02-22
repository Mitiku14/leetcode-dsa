class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = []
        for i in range(len(difficulty)):
            jobs.append((difficulty[i], profit[i]))
        jobs.sort()
        worker.sort()
        max_profit = 0
        j = 0
        total_profit = 0
        for ab in worker:
            while j < len(jobs) and jobs[j][0] <= ab:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            total_profit += max_profit
        
        return total_profit

