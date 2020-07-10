class Graph:
    def __init__(self,v):
        self.v = v
        self.graph = [[0 for i in range(v)]for j in range(v)]

    def addEdge(self,src,dest):
        self.graph[src][dest] = 1

    def isSafe(self,v,pos,path):
        if self.graph[path[pos-1]][v] == 0:
            return False
        for vertex in path:
            if vertex == v:
                return False
        return True

    def hamiltonUtil(self,pos,path):
        if pos == self.v:
            if self.graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False
        for v in range(1,self.v):
            if self.isSafe(v,pos,path) == True:
                path[pos] = v
                if self.hamiltonUtil(pos+1,path) == True:
                    return True
                path[pos] = -1
        return False

    def hamiltonCycle(self):
        path = [-1]*self.v
        path[0] = 0

        if self.hamiltonUtil(1,path) == False:
            return False
        for i in path:
            print(i,end = " ")
        print(path[0])
        return True

g1 = Graph(5)
g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0], ]
g1.hamiltonCycle()