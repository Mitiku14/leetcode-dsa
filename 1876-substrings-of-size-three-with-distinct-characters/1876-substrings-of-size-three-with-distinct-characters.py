class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        count = 0
        for r in range(2,len(s)):
            if len(set(s[l:r+1])) == 3:
                count += 1
            l += 1
        return count