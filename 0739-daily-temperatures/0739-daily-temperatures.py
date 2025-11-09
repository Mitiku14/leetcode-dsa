class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # tempIndex = {n:i for i, n in enumerate(temperatures)}
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):
            if not stack:
                stack.append(i)
            cur = temperatures[i]
            while stack and cur > temperatures[stack[-1]]:
                val = stack.pop()
                res[val] = i - val
            stack.append(i)
        return res

