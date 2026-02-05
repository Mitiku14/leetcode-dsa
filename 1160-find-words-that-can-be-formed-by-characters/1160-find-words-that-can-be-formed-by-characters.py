class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        i = 0
        count = 0
        count1 = 0
        for ch in words:
            
            c1 = Counter(ch)

            for i in range(len(ch)):
                
                if c1[ch[i]] <= cnt[ch[i]]:
                    
                    count1 += 1
                else:
                    count1 = 0
                    break
            count += count1
            count1= 0
            
        
        return count


        
       
                