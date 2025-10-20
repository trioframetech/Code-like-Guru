import heapq
from collections import defaultdict
from math import inf
from typing import List

MOD = 1_000_000_007

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v, w in roads:
            g[u].append((v, w))
            g[v].append((u, w))

        dist = [inf] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]  # (dist, node)
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(pq, (nd, v))
                elif nd == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n - 1] % MOD
