class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        score = 0
        for st in s:
            if st == '(':
                stack.append(score)
                score = 0
            elif stack:
                top = stack.pop()
                score = top + max(score * 2, 1)
        
        return score