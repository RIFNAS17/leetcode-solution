class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        if source == destination:
            return True
        visited = [False] * n
        def dfs(u):
            if u == destination:
                return True
            visited[u] = True
            for v in graph[u]:
                if not visited[v] and dfs(v):
                    return True
            return False
        return dfs(source)