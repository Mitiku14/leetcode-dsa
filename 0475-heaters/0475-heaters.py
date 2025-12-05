class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        i = j = 0 
        min_dist = 0
        while i < len(houses):
            while (j < (len(heaters) - 1)) and abs(heaters[j + 1] - houses[i]) <= abs(heaters[j] - houses[i]):
                j += 1
            min_dist = max(min_dist, abs(heaters[j] - houses[i]))
            i += 1
        return min_dist