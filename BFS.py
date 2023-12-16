# BFS

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")  # Выводим вершину на экран
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    print()  # Переходим на новую строку

# Пример графа
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Тестирование сортировки BFS
print("Результат сортировки BFS:")
bfs(graph, 'A')

def test_bfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    expected_output = "A B C D E F"
    actual_output = []
    
    # Перехватываем вывод на экран и сохраняем его в actual_output
    import sys
    sys.stdout = open('output.txt', 'w')
    bfs(graph, 'A')
    sys.stdout.close()
    
    # Считываем результат из файла
    with open('output.txt') as f:
        actual_output = f.read().strip()
    
    assert actual_output == expected_output, f"Ожидаемый вывод: {expected_output}, Фактический вывод: {actual_output}"
    print("Тест пройден успешно!")

test_bfs()