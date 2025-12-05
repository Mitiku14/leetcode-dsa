class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)
        for first, last, seats in bookings:
            res[first -1] += seats
            
            res[last] -= seats
        res2 = []
        cur = 0
        for i in range(n):
            cur += res[i]
            res2.append(cur)
        return res2