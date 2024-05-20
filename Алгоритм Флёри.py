# Алгоритм Флёри
def is_valid_next_edge(graph, u, v):
    # Проверяем, что ребро (u, v) существует
    if graph[u][v] == 0:
        return False

    # Считаем количество смежных вершин с u
    count = 0
    for i in range(len(graph[u])):
        if graph[u][i] != 0:
            count += 1

    # Если u имеет только одного соседа, это будет следующим ребром
    if count == 1:
        return True

    # Проверяем, что удаляя ребро (u, v) граф остается связным
    # Первоначально сохраняем граф
    temp = [[0] * len(graph[u]) for _ in range(len(graph))]
    for i in range(len(graph[u])):
        for j in range(len(graph)):
            temp[i][j] = graph[i][j]

    # Удаляем ребро (u, v) из графа
    graph[u][v] = graph[v][u] = 0

    # Считаем количество компонентов связности графа после удаления ребра
    visited = [False] * len(graph)
    current_component = 0
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited)
            current_component += 1

    # Восстанавливаем граф
    for i in range(len(graph[u])):
        for j in range(len(graph)):
            graph[i][j] = temp[i][j]

    # Если после удаления ребра граф остается связным, ребро (u, v) может быть следующим
    return current_component == 1


def dfs(graph, node, visited):
    # Помечаем текущую вершину как посещённую
    visited[node] = True

    # Рекурсивно обходим всех соседей текущей вершины
    for i in range(len(graph[node])):
        if graph[node][i] != 0 and not visited[i]:
            dfs(graph, i, visited)


def fleury_algorithm(graph):
    # Проверяем наличие эйлерова цикла
    if not is_eulerian(graph):
        return "Граф не содержит эйлерова цикла"

    # Копируем граф
    g = [[0] * len(graph[i]) for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            g[i][j] = graph[i][j]

    # Выбираем стартовую вершину u
    u = 0
    for i in range(len(graph)):
        if sum(graph[i]) % 2 != 0:
            u = i
            break

    # Инициализируем пустой стек и список для сохранения эйлерова цикла
    stack = []
    circuit = []

    # Помещаем стартовую вершину в стек
    stack.append(u)

    while len(stack) > 0:
        # Берем последнюю вершину из стека
        curr_node = stack[-1]

        # Ищем следующую вершину для обхода
        for next_node in range(len(graph[curr_node])):
            if is_valid_next_edge(g, curr_node, next_node):
                break

        # Если нет доступного ребра, добавляем текущую вершину в эйлеров цикл и удаляем ее из стека
        if next_node == len(graph[curr_node]):
            circuit.append(stack.pop())
        else:
            # Если есть доступное ребро, добавляем его в эйлеров цикл и в стек удаляем ребро из графа
            stack.append(next_node)
            g[curr_node][next_node] = g[next_node][curr_node] = 0

    # Обратный порядок вершин свидетельствует об эйлеровом цикле
    circuit.reverse()

    return circuit


def is_eulerian(graph):
    # Проверяем, что граф связный
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited)
            break
    if False in visited:
        return False

    # Проверяем, что каждая вершина имеет четную степень
    for node in graph:
        if sum(node) % 2 != 0:
            return False

    return True


# Пример работы алгоритма
graph = [[0, 1, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 0, 1, 0],
         [0, 1, 1, 0, 1],
         [1, 1, 0, 1, 0]]

eulerian_cycle = fleury_algorithm(graph)
print(eulerian_cycle)


# Тест
def test_fleury_algorithm():
    # Тест 1: Граф содержит эйлеров цикл
    graph1 = [[0, 1, 1, 0, 1],
              [1, 0, 1, 1, 1],
              [1, 1, 0, 1, 0],
              [0, 1, 1, 0, 1],
              [1, 1, 0, 1, 0]]
    assert fleury_algorithm(graph1) == [0, 1, 2, 3, 1, 4, 3, 0]
 # Тест 2: Граф не содержит эйлеров цикл
    graph2 = [[0, 1, 1, 0, 1],
              [1, 0, 1, 1, 1],
              [1, 1, 0, 1, 1],
              [0, 1, 1, 0, 1],
              [1, 1, 1, 1, 0]]
    assert fleury_algorithm(graph2) == "Граф не содержит эйлерова цикла"

    # Тест 3: Граф состоит из одной вершины
    graph3 = [[0]]
    assert fleury_algorithm(graph3) == [0]
   
    # Тест 4: Граф содержит две вершины со связью
    graph4 = [[0, 1],
              [1, 0]]
    assert fleury_algorithm(graph4) == [0, 1, 0]

    # Тест 5: Граф не содержит ребер
    graph5 = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    assert fleury_algorithm(graph5) == "Граф не содержит эйлерова цикла"
  
    print("Все тесты успешно пройдены!")


test_fleury_algorithm()