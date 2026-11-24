class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        dist = [[10001] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for a, b, w in edges:
            dist[a][b] = w
            dist[b][a] = w
        for k in range(n):
            dk = dist[k]
            for i in range(n):
                di = dist[i]
                dik = di[k]
                for j in range(n):
                    v = dik + dk[j]
                    if v < di[j]:
                        di[j] = v
        min_reachable = n
        result = -1
        for i in range(n):
            di = dist[i]
            reachable = 0
            for j in range(n):
                if di[j] <= distanceThreshold:
                    reachable += 1
            if reachable <= min_reachable:
                min_reachable = reachable
                result = i
        return result