class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        n = len(s1)
        for i in range(n - 2):
            if s1[i] != s2[i]:
                s1[i] , s1[i + 2] = s1[i + 2], s1[i]

        
        if ''.join(s1) == ''.join(s2):
            return True
        return False