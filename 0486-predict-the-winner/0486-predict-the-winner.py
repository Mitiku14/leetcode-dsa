class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def predWinner(nums, l, r, n):
            if l == r:
                return nums[l]
            
            left = nums[l] - predWinner(nums, l + 1, r, n)
            right = nums[r] - predWinner(nums, l, r -1, n)
            return max(left, right)
        
        n = len(nums)
        res = predWinner(nums, 0, n - 1, n)
        return True if res >= 0 else False

            


            
            

            


