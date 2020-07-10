#Kosaraju's Algorithm

from collections import defaultdict

def DFS_fill_stack(visited, stack, graph, v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            DFS_fill_stack(visited, stack, graph, i)

    stack.append(v)


def transposeG(G):
    gTrans = defaultdict(list)

    for vertex in G:
        for adjacencyVertex in G[vertex]:
            gTrans[adjacencyVertex].append(vertex)

    return gTrans


def DFS_print_SCCs(visited, graph, v):
    visited[v] = True

    for adjacencyVertex in graph[v]:
        if not visited[adjacencyVertex]:
            DFS_print_SCCs(visited, graph, adjacencyVertex)



def countSCCs(g,V):
    visited = [False] * V
    stack = []

    for i in range(V):
        if not visited[i]:
            DFS_fill_stack(visited, stack, g, i)

    gTrans = transposeG(g)

    ans = 0
    visited = [False] * V
    while len(stack) != 0:
        elem = stack.pop()
        if not visited[elem]:
            DFS_print_SCCs(visited, gTrans, elem)
            ans += 1
            # print()

    return ans