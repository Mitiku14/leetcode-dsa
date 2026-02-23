class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        max_h = 0
        for i in range(n):
            if citations[i] >= i + 1:
                max_h = max(max_h, i + 1)
        return max_h


        

