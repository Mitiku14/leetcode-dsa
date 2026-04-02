class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mapp = set(wordDict)
        # @cache or using memo
        memo = {}

        def backtrack(idx):
            if idx >= len(s):
                return True
            if idx in memo:
                return memo[idx]
            
            cur = ""
            for i in range(idx, len(s)):
                cur += s[i]
                if cur in mapp:
                    if backtrack(i + 1):
                        memo[idx] = True
                        return True
            memo[idx] = False
            return False
        return backtrack(0)

