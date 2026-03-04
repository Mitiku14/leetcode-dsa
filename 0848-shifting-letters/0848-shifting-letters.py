class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        cur = 0
        res = []
        n = len(shifts)
        for i in range(n -1, -1, -1):
            cur += shifts[i]
            new_char = (ord(s[i]) - ord('a') + cur) % 26
            res.append(chr(new_char + ord('a')))
        return ''.join(res[::-1])
