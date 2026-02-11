class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)
        res = ""
        for i in range(1, len(s)):
            if int(s[i]) != int(s[i-1]) and int(s[i]) == cnt[s[i]] and int(s[i-1]) == cnt[s[i-1]]:
                print(s[i], s[i-1])
                res += s[i-1: i+1]
                return res
            
        return ""