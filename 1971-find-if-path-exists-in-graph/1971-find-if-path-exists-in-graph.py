class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set([source])
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for ng in graph[node]:
                if ng not in visited:
                    stack.append(ng)
                    visited.add(ng)
        return False
        
        
