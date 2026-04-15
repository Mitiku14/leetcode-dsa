class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        k = startIndex
        n = len(words)
        short_dist = float('inf')
        for i in range(n):
            ind = (i + startIndex) % n
            if words[ind] == target:
                short_dist = min(short_dist, i)
        for i in range(n):
            ind = (startIndex - i) % n

            if words[ind] == target:
                short_dist = min(short_dist, i)
        return short_dist if short_dist != float('inf') else -1 
        
