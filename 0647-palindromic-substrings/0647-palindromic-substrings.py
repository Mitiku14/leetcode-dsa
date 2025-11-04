class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count =0
        for i in range(n):
            j = i + 1
            while j < n:
                if s[i] == s[j]:
                    count += 1
                j += 1
        return n + count if count else n