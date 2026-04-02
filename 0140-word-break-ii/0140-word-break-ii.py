class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mapp = set(wordDict)

        res = []
        def backtrack(idx, cur):
            if idx >= len(s):
                res.append(' '.join(cur))
                return 
            
            temp = ""
            for i in range(idx, len(s)):
                temp += s[i]
                if temp in mapp:
                    backtrack(i + 1, cur + [temp])
            
            return 
        backtrack(0, [])
        return res