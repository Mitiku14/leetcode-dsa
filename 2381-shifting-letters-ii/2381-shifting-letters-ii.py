class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for L, R, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[L] += val
            if R + 1 < n:
                diff[R + 1] -= val
        prefix = 0
        result = []
        for i in range(n):
            prefix += diff[i]
            new_char_index = (ord(s[i]) - ord('a') + prefix) % 26
            result.append(chr(new_char_index + ord('a')))
        return "".join(result)

