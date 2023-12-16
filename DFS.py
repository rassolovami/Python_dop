# DFS

def dfs_sort(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_sort(graph, neighbor, visited)
    return visited

def test_dfs_sort():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    assert dfs_sort(graph, 'A') == {'A', 'B', 'D', 'E', 'F', 'C'}
    assert dfs_sort(graph, 'B') == {'B', 'D', 'E', 'F'}
    assert dfs_sort(graph, 'D') == {'D'}
    assert dfs_sort(graph, 'F') == {'F'}
    assert dfs_sort(graph, 'C') == {'C', 'F'}
    print("Тесты пройдены успешно!")


test_dfs_sort()