class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        for i in range(1, n):
            temp = prices[i] - prices[i -1]
            if temp > 0:
                ans += temp
        
        return ans