class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        par = [i for i in range(n)]
        size = [1] * n

        def find(node):
            if node == par[node]:
                return node
            p = find(par[node])
            par[node] = p
            return p
        
        def union(u, v):
            u = find(u)
            v = find(v)
            if u != v:
                if size[u] < size[v]:
                    u, v = v, u
                par[v] = u
                size[u] += size[v]
        
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 1:
                    union(i, j)
        seen = set()
        for node in range(n):
            seen.add(find(node))
        return len(seen)


        