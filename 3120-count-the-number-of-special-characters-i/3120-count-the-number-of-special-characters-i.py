class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        st = list(set(word))
        cnt = 0
        for s in st:
            if s.islower():
                x = s.upper()
                if x in st:
                    cnt += 1
            
        return cnt
            
        
