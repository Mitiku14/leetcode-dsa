class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white, gray, black = 1, 2, 3
        color = {i: white for i in range(numCourses)}
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[b].append(a)
        finish = True
        def dfs(node):
            nonlocal finish
            if not finish:
                return

            color[node] = gray

            for neighbor in adj[node]:
                if color[neighbor] == white:
                    dfs(neighbor)
                elif color[neighbor] == gray:
                    finish = False
                    return

            color[node] = black
        for i in range(numCourses):
            if color[i] == white:
                dfs(i)

        return finish