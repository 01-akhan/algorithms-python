from typing import Dict, List, Tuple
from collections import deque
import heapq

AdjList = Dict[int, List[int]]
WeightedAdj = Dict[int, List[Tuple[int, int]]]  # node -> [(neighbor, weight)]

def bfs(adj: AdjList, start: int) -> List[int]:
    visited = set([start])
    order: List[int] = []
    q = deque([start])
    while q:
        v = q.popleft()
        order.append(v)
        for u in adj.get(v, []):
            if u not in visited:
                visited.add(u)
                q.append(u)
    return order

def dfs(adj: AdjList, start: int) -> List[int]:
    visited = set()
    order: List[int] = []
    stack = [start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        order.append(v)
        for u in reversed(adj.get(v, [])):
            if u not in visited:
                stack.append(u)
    return order

def dijkstra(adj: WeightedAdj, source: int) -> Dict[int, int]:
    INF = 10**18
    dist: Dict[int, int] = {v: INF for v in adj.keys()}
    dist[source] = 0
    pq: List[Tuple[int, int]] = [(0, source)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u, w in adj.get(v, []):
            nd = d + w
            if nd < dist.get(u, INF):
                dist[u] = nd
                heapq.heappush(pq, (nd, u))
    return dist