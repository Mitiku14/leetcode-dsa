class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        par = [i for i in range(n)]
        size = [1] * n

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
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


        