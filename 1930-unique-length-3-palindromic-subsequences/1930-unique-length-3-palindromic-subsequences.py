class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        print(set(s))
        for ch in set(s):
            L = s.find(ch)
            R = s.rfind(ch)
            if R - L < 2:
                continue 
            middle_chars = set(s[L+1:R])
            result += len(middle_chars)

        return result
