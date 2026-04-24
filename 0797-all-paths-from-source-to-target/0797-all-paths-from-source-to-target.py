class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        n = len(graph)
        dest = n - 1
        res = []
        edge = defaultdict(list)
        for i in range(n):
            for j in range(len(graph[i])):
                edge[i].append(graph[i][j])
        def dfs(node, path):
            if node == dest:
                res.append(path.copy())
                return 
            for ng in edge[node]:
                path.append(ng)
                dfs(ng, path)
                path.pop()
        dfs(source, [source])
        return res
        
                 
        
                
                    










