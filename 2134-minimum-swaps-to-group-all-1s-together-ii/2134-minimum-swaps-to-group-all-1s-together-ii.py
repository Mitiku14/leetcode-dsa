class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = nums.count(1)
        if total_ones == n and total_ones == 0:
            return 0
        nums_ext = nums + nums
        left, max_ones = 0, 0
        one_in_window = 0
        for r in range(len(nums_ext)):
            if nums_ext[r] == 1:
                one_in_window += 1
            if r - left + 1 > total_ones:
                if nums_ext[left] == 1:
                    one_in_window -= 1
                left += 1
            if r - left + 1 == total_ones:
                max_ones = max(max_ones, one_in_window)
        return total_ones - max_ones
            