class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for key, value in enumerate(s):
            if count[value] == 1:
                return key 
                break
        return -1
       
        