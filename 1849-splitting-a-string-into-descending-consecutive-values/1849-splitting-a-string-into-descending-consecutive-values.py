class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(ind, prev):
            if ind == len(s):
                return True
            cur_num = 0
            for j in range(ind, len(s)):
                cur_num = cur_num * 10 + int(s[j])

                if cur_num == prev - 1:
                    if backtrack(j + 1, cur_num):
                        return True

            return False

        for i in range(len(s) - 1):
            first = int(s[:i + 1])
            if backtrack(i + 1, first):
                return True

        return False