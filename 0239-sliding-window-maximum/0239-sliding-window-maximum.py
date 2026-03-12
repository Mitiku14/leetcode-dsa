class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        l = 0
        for i in range(len(nums)): 
            while dq and i - dq[0][1] + 1 > k:
                dq.popleft()
                l += 1

            while dq and nums[i] > dq[-1][0]:
                dq.pop()
            
            dq.append((nums[i], i))
            if i + 1 >= k:

                res.append(dq[0][0])
        return res