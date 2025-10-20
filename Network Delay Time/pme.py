import heapq
from math import inf
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Dijkstra from source k
        dist = [inf] * (n + 1)
        dist[k] = 0
        pq = [(0, k)]  # (distance_so_far, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue  # skip stale heap entries

            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        # Ignore index 0 (1-indexed nodes). If some node is unreachable, its dist is inf.
        ans = max(dist[1:])
        return -1 if ans == inf else int(ans)
