class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        cnt = defaultdict(set)
        for i in range(len(s) - k + 1):
            cnt[s[i:k+i]] = 1

        if len(cnt) == 2 **k:
            return True
        return False