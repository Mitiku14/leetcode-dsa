class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        left = 0
        right = 0
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid
     
        right = r

        l= 0
        r = n - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        left = l
        print([left, right])
        if left and  right:
            return [right, left]
        return [-1, -1]