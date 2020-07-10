import heapq
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,src,dest,dist):
        self.graph[src].append((dest,dist))

    def calculate_distances(self, graph, starting_vertex):
        distances = {vertex: float('infinity') for vertex in graph}
        distances[starting_vertex] = 0

        pq = [(0, starting_vertex)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)

            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight

                # Only consider this new path if it's better than any path we've
                # already found.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

g = Graph()

g.addEdge("u","v",2)
g.addEdge("u","w",5)
g.addEdge("u","x",1)
g.addEdge("v","u",2)
g.addEdge("v","x",2)
g.addEdge("v","w",2)
g.addEdge("w","v",3)
g.addEdge("w","u",5)
g.addEdge("w","x",3)
g.addEdge("w","y",1)
g.addEdge("w","z",5)
g.addEdge("x","u",1)
g.addEdge("x","v",2)
g.addEdge("x","w",3)
g.addEdge("x","y",1)
g.addEdge("y","x",1)
g.addEdge("y","w",1)
g.addEdge("y","z",1)
g.addEdge("z","w",5)
g.addEdge("z","y",1)

print(g.calculate_distances(g.graph,"x"))
