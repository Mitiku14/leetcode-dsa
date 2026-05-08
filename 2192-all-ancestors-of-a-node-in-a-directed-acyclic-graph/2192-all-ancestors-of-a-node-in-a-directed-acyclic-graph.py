
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indeg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1
        ancestors = [set() for _ in range(n)]
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
    
        while q:
            node = q.popleft()
            for nei in graph[node]:
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
    
        res = []
        for s in ancestors:
            res.append(sorted(s))
        return res