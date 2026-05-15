class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        size = [1] * (n + 1)
        def find(node):
            if par[node] != node:
                par[node] = find(par[node])
            return par[node]
        def union(u, v):
            ur = find(u)
            uv = find(v)
            if ur == uv:
                return 
            if size[ur] < size[uv]:
                ur, uv = uv, ur
            par[uv] = ur
            size[ur] += size[uv]
        res = []
        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            union(u, v)