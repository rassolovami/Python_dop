# Алгоритм Косарайю

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFS(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i, visited)

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        
        stack.append(v)
    
    def getTranspose(self):
        g = Graph(self.V)
        
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        
        return g
    
    def printSCCs(self):
        stack = []
        visited = [False] * (self.V)
        
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        
        gr = self.getTranspose()
        
        visited = [False] * (self.V)
        
        while stack:
            i = stack.pop()
            
            if visited[i] == False:
                gr.DFS(i, visited)
                print()
                
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print("Following are strongly connected components in the graph:")
g.printSCCs()