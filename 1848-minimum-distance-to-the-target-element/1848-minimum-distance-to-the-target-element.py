class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        min_abs = float('inf')
        ind = 0
        for i in range(n):
            if nums[i] == target:
                temp = abs(i - start)
                if temp <= min_abs:
                    min_abs = temp

        return min_abs 
