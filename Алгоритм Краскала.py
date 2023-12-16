# Алгоритм Краскала

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Функция для поиска корня множества элемента i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Функция для объединения двух множеств по их рангу
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Основная функция алгоритма Краскала
    def kruskal(self):
        result = []

        # Сортировка всех ребер графа в порядке неубывания веса
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.num_vertices):
            parent.append(node)
            rank.append(0)

        i = 0
        e = 0

        while e < self.num_vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Минимальное остовное дерево:")
        for u, v, weight in result:
            print(f"{u} - : {weight}")

# Тестирование алгоритма Краскала
g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 7)

g.kruskal()

