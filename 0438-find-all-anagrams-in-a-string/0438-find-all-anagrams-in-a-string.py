class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter()
        res = []
        k = len(p)
        for r in range(len(s)):
            s_count[s[r]] += 1
            if r >= k:
                left_char = s[r - k]
                s_count[left_char] -= 1
                if s_count[left_char] == 0:
                    del s_count[left_char]
            if s_count == p_count:
                res.append(r -k + 1)
        return res
        
