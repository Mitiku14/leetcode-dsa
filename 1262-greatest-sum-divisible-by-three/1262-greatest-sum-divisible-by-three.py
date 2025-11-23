class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total =0
        remain_one = float("inf")
        remain_two = float("inf")
        for n in nums:
            total += n
            if n % 3 == 1:
                remain_two = min(remain_two, n + remain_one)
                remain_one = min(remain_one,n)
            if n % 3 == 2:
                remain_one = min(remain_one, n + remain_two)
                remain_two = min(remain_two, n)
        

        if total % 3 == 0:
            return total
        if total % 3 == 1:
            return total - remain_one
        if total % 3 == 2:
            return total - remain_two


    
            
        

