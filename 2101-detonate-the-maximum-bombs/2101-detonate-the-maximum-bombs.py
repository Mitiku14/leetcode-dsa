
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2:
                    graph[i].append(j)
        def bfs(start):
            queue = deque([start])
            visited = set([start])
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

            return len(visited)
        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
        return ans