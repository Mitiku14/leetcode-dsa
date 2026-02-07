class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        sorted_items = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        res = ""
        for key , val in sorted_items:
            res += key * val
        return res



