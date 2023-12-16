# Алгоритм Тарьяна 

from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)
        self.visited = [False] * num_vertices
        self.stack = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v):
        self.visited[v] = True

        for neighbor in self.graph[v]:
            if not self.visited[neighbor]:
                self.topological_sort_util(neighbor)

        self.stack.append(v)

    def topological_sort(self):
        for i in range(self.num_vertices):
            if not self.visited[i]:
                self.topological_sort_util(i)

        return self.stack[::-1]

# Тест алгоритма

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:")
print(g.topological_sort())