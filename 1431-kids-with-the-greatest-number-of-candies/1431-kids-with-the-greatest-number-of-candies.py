class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxVla = max(candies)
        for i in range(len(candies)):
            total = candies[i] + extraCandies
            print(total)
            if total < maxVla:
                res.append(False)
            elif total >= maxVla:
                res.append(True)
        return res
        
