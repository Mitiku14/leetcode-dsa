class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n,m  = len(word1), len(word2)
        i = j = 0
        while i < n and j < m:
            res += word1[i]
            res += word2[i]
            i += 1
            j += 1
        res += word1[i:] + word2[j:]
        return res