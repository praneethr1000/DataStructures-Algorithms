from collections import defaultdict


# This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def checkForPath(self,src,dest,path=[]):
        graph = self.graph
        path = path + [src]
        if src == dest:
            return path
        if src not in graph:
            return None
        for vertex in graph[src]:
            if vertex not in path:
                extendedPath = self.checkForPath(vertex,dest,path)
                if extendedPath:
                    return extendedPath
        return None



# Create a graph given in the above diagram
g = Graph(6)
g.addEdge("a", "b")
g.addEdge("a", "c")
g.addEdge("b", "d")
g.addEdge("b", "e")
g.addEdge("c", "d")
g.addEdge("d", "e")
g.addEdge("e", "a")

print(g.checkForPath("a","e"))
