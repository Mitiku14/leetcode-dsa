class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_bracket = 0
        res = ""
        for st in s:
            if st == "(":
                if open_bracket > 0:
                    res += st
                open_bracket += 1
            else:
                open_bracket -= 1
                if open_bracket > 0:
                    res += st
        return res