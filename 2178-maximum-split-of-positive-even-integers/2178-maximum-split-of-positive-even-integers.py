class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        res = []
        total = 0
        next_even = 2
        while total + next_even <= finalSum:
            res.append(next_even)
            total += next_even
            next_even += 2
        
        if total < finalSum:
            res[-1] += (finalSum - total )
        return res

        