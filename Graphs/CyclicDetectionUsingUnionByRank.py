# union by rank and path compression based implementation to find a cycle in a graph
from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    # path compression technique
    def find(self,subsets,vertex):
        if subsets[vertex].parent != vertex:
            subsets[vertex].parent = self.find(subsets, subsets[vertex].parent)
        return subsets[vertex].parent

    def union(self, subsets, u, v):
        if subsets[u].rank > subsets[v].rank:
            subsets[v].parent = u
        elif subsets[v].rank > subsets[u].rank:
            subsets[u].parent = v
        else:
            subsets[v].parent = u
            subsets[u].rank += 1

    def isCyclic(self):
        subsets = []
        for i in range(self.v):
            subsets.append(Subset(i,0))

        for vertex in self.graph:
            vertex_parent = self.find(subsets,vertex)
            for adjVertex in self.graph[vertex]:
                adjVertex_parent = self.find(subsets,adjVertex)

                if vertex_parent == adjVertex_parent:
                    return True
                else:
                    self.union(subsets,vertex_parent,adjVertex_parent)

        return False

class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
if g.isCyclic():
    print('Graph contains cycle')
else:
    print('Graph does not contain cycle')

g1 = Graph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)
if g1.isCyclic():
    print('Graph contains cycle')
else:
    print('Graph does not contain cycle')


