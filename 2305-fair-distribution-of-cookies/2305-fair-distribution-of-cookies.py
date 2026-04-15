class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfair = float('inf')
        n = len(cookies)
        min_diff = 0

        children = [0] * k
        def backtrack(ind, children):
            nonlocal min_unfair
            if ind >=n:
                unfair = max(children)
                min_unfair = min(min_unfair, unfair)
                return 
            for i in range(k):
                children[i] += cookies[ind]
                backtrack(ind + 1, children)
                children[i] -= cookies[ind]
                if children[i] == 0:
                    break


        backtrack(0, children)
        return min_unfair
        
            

