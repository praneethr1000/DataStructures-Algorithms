from collections import deque
import sys

row = [-1,1,0,0]
col = [0,0,1,-1]

def valid(i,j,m,n,visited):
    return i >=0 and i < m and j >=0 and j < n and visited[i][j] == False

def shortestPath(srcI,srcJ,posI,posJ,n,m,a):
    global row, col
    if posI == srcI and posJ == srcJ:
        return a[posI][posJ]
    visited = [[False]*n for i in range(n)]
    q = deque()
    q.append((srcI,srcJ,a[srcI][srcJ]))
    visited[srcI][srcJ] = True
    while q:
        currI, currJ, dist = q.popleft()
        if posI == currI and posJ == currJ:
            return dist
        k = sys.maxsize
        reqI = -1
        reqJ = -1
        for i in range(4):
            presI = currI + row[i]
            presJ = currJ + col[i]
            if valid(presI,presJ,n,m,visited):
                visited[presI][presJ] = True
                if presI == posI and presJ == posJ:
                    k = a[presI][presJ]
                    reqI = presI
                    reqJ = presJ
                    break
                if a[presI][presJ] < k:
                    k = a[presI][presJ]
                    reqI = presI
                    reqJ = presJ
        if reqI != -1 and reqJ != -1:
            q.append((reqI,reqJ,dist+k))

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    k = 0
    a = []
    for i in range(0,len(l),n):
        a.append(l[i:i+n])
    print(shortestPath(0,0,n-1,n-1,n,n,a))


'''
Sample Input:

2
5
31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20
2
42 93 7 14

'''