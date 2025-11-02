class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = [num ** 2 for num in nums]
        return sorted(square)