class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        par = [i for i in range(n)]
        size = [1] * n
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(a,b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return 
            if par[ra] < par[rb]:
                ra, rb = rb, ra
            par[rb] = ra
            size[ra] += size[rb]
        cnt =0
        for u, v in connections:
            union(u, v)
        cnt = 0
        for i in range(n):
            if find(i) == i:
                cnt += 1
        
        return cnt - 1
