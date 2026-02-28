class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start , max_len, max_repeat_letter_count = 0, 0, 0
        freq_map = {}
        for end in range(len(s)):
            right_char = s[end]
            if right_char not in freq_map:
                freq_map[right_char]  = 0
            freq_map[right_char] += 1
            max_repeat_letter_count = max(max_repeat_letter_count, freq_map[right_char])

            if (end - start + 1 - max_repeat_letter_count) > k:
                left_char = s[start]
                freq_map[left_char] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        
        return max_len

