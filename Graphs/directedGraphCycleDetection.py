from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    #Using DFS

    def cyclicUtil(self,visited,recVisited,i):
        visited[i] = True
        recVisited[i] = True
        for v in self.graph[i]:
            if visited[v] == False:
                if self.cyclicUtil(visited,recVisited,v):
                    return True
            elif recVisited[v] == True:
                return True
        recVisited[v] = False
        return False

    def isCyclic(self):
        visited = [False]*self.v
        recVisited = [False] * self.v
        for i in range(self.v):
            if visited[i] == False:
                if self.cyclicUtil(visited,recVisited,i):
                    return True
        return False

    #Using Colors

    def cyclicColors(self,vertex,colors):
        colors[vertex] = "grey"
        for v in self.graph[vertex]:
            if colors[v] == "grey":
                return True
            if colors[v] == "white":
                if self.cyclicColors(v,colors):
                    return True
        colors[vertex] = "black"
        return False


    def cyclic(self):
        colors = ["white"]*self.v
        for i in range(self.v):
            if colors[i] == "white":
                if self.cyclicColors(i,colors):
                    return True
        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.cyclic())
print(g.isCyclic())