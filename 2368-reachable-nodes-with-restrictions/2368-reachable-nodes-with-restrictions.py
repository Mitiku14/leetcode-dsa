class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        if 0 in restricted:
            return 0
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = deque([0])
        count = 1
        visited = set([0])
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei in restricted:
                    continue
                if nei not in visited:
                    q.append(nei)
                    
                    visited.add(nei)
                    count += 1
        return count
            

