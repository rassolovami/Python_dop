# Алгоритм  Флойда-Уоршелла
def floyd_warshall(graph):
    distance = graph.copy()
    n = len(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

# Пример использования
inf = float('inf')
graph = [
    [0, inf, -2, inf],
    [4, 0, 3, inf],
    [inf, inf, 0, 2],
    [inf, -1, inf, 0]
]

result = floyd_warshall(graph)
print(result)

def test_floyd_warshall():
    inf = float('inf')
    graph = [
        [0, inf, -2, inf],
        [4, 0, 3, inf],
        [inf, inf, 0, 2],
        [inf, -1, inf, 0]
    ]

    expected_result = [
        [0, 2, -2, 0],
        [4, 0, 2, 4],
        [5, 7, 0, 2],
        [3, -1, 1, 0]
    ]

    result = floyd_warshall(graph)
    assert result == expected_result, "Алгоритм Флойда-Уоршелла работает некорректно"

test_floyd_warshall()
print("Все тесты пройдены успешно")