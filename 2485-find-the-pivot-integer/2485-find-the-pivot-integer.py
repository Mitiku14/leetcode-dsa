class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        leftSum = 0
        for i in range(1,n+1):
            rightSum = total - leftSum - i
            if rightSum == leftSum:
                return i
            leftSum += i
        return -1



