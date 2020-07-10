from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def DFS(self,vertex,visited,parent):
        visited[vertex] = True
        for i in self.graph[vertex]:
            if visited[i] == False:
                if self.DFS(i,visited,vertex):
                    return True
            elif parent != i:
                return True
        return False


    def cyclic(self):
        visited = [False] * self.v
        for vertex in range(self.v):
            if visited[vertex] == False:
                if self.DFS(vertex,visited,-1) == True:
                    return True
        return False

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
print(g.cyclic())