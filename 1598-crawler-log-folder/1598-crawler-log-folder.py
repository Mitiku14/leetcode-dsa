class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for ch in logs:
            if ch == './':
                continue
            elif ch == '../' :
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return len(stack)