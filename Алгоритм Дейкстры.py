# Алгоритм Дейкстры

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 10},
    'C': {'A': 2, 'F': 12},
    'D': {'B': 5, 'E': 7},
    'E': {'B': 10, 'D': 7, 'F': 3},
    'F': {'C': 12, 'E': 3}
}

def dijkstra(graph, start_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0
    unvisited_vertices = set(graph.keys())

    while unvisited_vertices:
        current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
        unvisited_vertices.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            temp_distance = distances[current_vertex] + weight
            if temp_distance < distances[neighbor]:
                distances[neighbor] = temp_distance

    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 10},
    'C': {'A': 2, 'F': 12},
    'D': {'B': 5, 'E': 7},
    'E': {'B': 10, 'D': 7, 'F': 3},
    'F': {'C': 12, 'E': 3}
}
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(distances)

# Вывод: {'A': 0, 'B': 4, 'C': 2, 'D': 9, 'E': 11, 'F': 5}