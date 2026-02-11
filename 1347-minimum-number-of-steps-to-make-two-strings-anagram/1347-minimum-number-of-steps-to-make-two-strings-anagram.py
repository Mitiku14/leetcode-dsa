class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        if count_s == count_t:
            return 0
        for ch in t:
            if ch not in count_s:
                continue
            elif  ch in count_s:
                count_s[ch] -= 1
                count_t[ch] -= 1
                if count_t[ch] == 0:
                    del count_t[ch]
                if count_s[ch] == 0:
                    del count_s[ch]
        count = 0
        for val in count_t.values():
            count += val
        return count



        
            
            
                    