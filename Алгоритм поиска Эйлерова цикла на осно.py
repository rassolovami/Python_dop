# Алгоритм поиска Эйлерова цикла на основе объединения простых циклов

def find_eulerian_cycle(graph):
    # Инициализация пустого стека для хранения цикла
    stack = []
    
    # Инициализация пустого списка для хранения Эйлерова цикла
    eulerian_cycle = []
    
    # Добавление первой вершины в стек
    stack.append(0)
    
    while len(stack) != 0:
        # Если у текущей вершины есть соседи
        if len(graph[stack[-1]]) != 0:
            # Добавляем текущую вершину в стек
            stack.append(graph[stack[-1]].pop())
        else:
            # Если у текущей вершины нет соседей, добавляем её в Эйлеров цикл
            eulerian_cycle.append(stack.pop())
    
    # Переворачиваем список, чтобы получить правильный порядок вершин в Эйлеровом цикле
    eulerian_cycle.reverse()
    
    return eulerian_cycle

# Проверяемый граф
graph = {0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1], 3: [1, 4], 4: [1, 3]}

# Вызов функции поиска Эйлерова цикла
eulerian_cycle = find_eulerian_cycle(graph)

# Вывод найденного Эйлерова цикла
print("Eulerian Cycle:", eulerian_cycle)
