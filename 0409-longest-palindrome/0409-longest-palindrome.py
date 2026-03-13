class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        long_pal = 0
        odd_exists = False
        for ch, count in cnt.items():
            if count % 2 == 0:
                long_pal += count
            else:
                long_pal += count -1
                odd_exists = True
            
        
        if odd_exists:
            return long_pal + 1
        return long_pal

