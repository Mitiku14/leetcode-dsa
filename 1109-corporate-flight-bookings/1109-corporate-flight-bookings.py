class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pref = [0] * (n + 1)
        for f, l , s in bookings:
            pref[f -1] += s
            pref[l] -= s
        ans = []
        cur = 0
        for i in range(n):
            cur += pref[i]
            ans.append(cur)
        return ans