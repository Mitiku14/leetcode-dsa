class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # n = floor(c/2) + 1
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if i *i + j * j == c:
        #             return True
        # return False
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            if left * left + right * right == c:
                return True
                
            elif left * left + right * right > c:
                right -= 1
            else:
                left += 1
        return False