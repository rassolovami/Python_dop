# Алгоритм Прима

from collections import defaultdict
import heapq

def prim(graph):
    min_spanning_tree = defaultdict(set)
    visited = set()
    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    edges = [
        (cost, start_vertex, to)
        for to, cost in graph[start_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, from_vertex, to_vertex = heapq.heappop(edges)
        if to_vertex not in visited:
            visited.add(to_vertex)
            min_spanning_tree[from_vertex].add(to_vertex)
            for to, cost in graph[to_vertex].items():
                if to not in visited:
                    heapq.heappush(edges, (cost, to_vertex, to))

    return min_spanning_tree

# Пример использования
graph = {
    'A': {'B': 10, 'C': 6, 'D': 5},
    'B': {'A': 10, 'E': 15},
    'C': {'A': 6, 'D': 4, 'F': 9},
    'D': {'A': 5, 'C': 4, 'E': 12, 'F': 8},
    'E': {'B': 15, 'D': 12, 'F': 7},
    'F': {'C': 9, 'D': 8, 'E': 7}
}

min_spanning_tree = prim(graph)
print(min_spanning_tree)

graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'D': 3},
    'C': {'A': 2, 'D': 4},
    'D': {'B': 3, 'C': 4}
}

