from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,src,dest):
        self.graph[src].append(dest)

    def find_shortest_paths(self,src):
        parent = {src: None}
        distance = {src: 0}
        visited = set()
        que = []
        que.append(src)
        visited.add(src)
        while que:
            s = que.pop(0)
            for dest in self.graph[s]:
                if dest not in visited:
                    visited.add(dest)
                    parent[dest] = s
                    distance[dest] = distance[s] + 1
                    que.append(dest)
        print('Path from destination vertices to source vertex {}:'.format(src))
        for v in parent:
            print('Vertex {} (distance {}): '.format(v, distance[v]),
                  end='')
            while parent[v] is not None:
                print(v, end=' ')
                v = parent[v]
            print(src)  # print source vertex


g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.find_shortest_paths(1)
