class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # we use shell sort for this quesion 
        
        gap = n//2
        while gap > 0:
            for i in range(gap, n):
                temp = nums[i]
                j = i
                while j >= gap and nums[j-gap] > temp:
                    nums[j] = nums[j-gap]
                    j -= gap
                nums[j] = temp
            gap //= 2
        return nums
                