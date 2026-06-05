class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        half = n // 2

        st = list(set(candyType))
        return len(st) if len(st) <= half else min(len(st), half)