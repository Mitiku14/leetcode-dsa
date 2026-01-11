from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(curr, target, visited):
            if curr not in graph:
                return -1.0
            if curr == target:
                return 1.0

            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return weight * res

            return -1.0

        
        results = []
        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(a, b, set()))

        return results
