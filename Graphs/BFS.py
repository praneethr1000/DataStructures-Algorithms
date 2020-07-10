from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    def BFS(self,s):
        visited = [False]*(len(self.graph))
        que = []
        que.append(s)
        visited[s] = True
        while que:
            s = que.pop(0)
            print(s,end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    que.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3) 
g.BFS(2)
