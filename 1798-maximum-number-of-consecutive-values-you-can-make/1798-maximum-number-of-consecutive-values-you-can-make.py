class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        max_make = 0
        for coin in coins:
            if coin <= max_make + 1:
                max_make += coin
            else:
                break
        
        return max_make + 1
