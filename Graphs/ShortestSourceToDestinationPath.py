from collections import deque

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]


def valid(i, j, n, m):
    return i >= 0 and i < n and j >= 0 and j < m


def shortestPath(srcI, srcJ, posI, posJ, n, m, a):
    global row, col
    visited = [[False] * m for i in range(n)]
    if a[srcI][srcJ] != 1 or a[posI][posJ] != 1:
        return -1
    q = deque()
    q.append((srcI, srcJ, 0))
    visited[srcI][srcJ] = True
    while q:
        currI, currJ, dist = q.popleft()
        if currI == posI and currJ == posJ:
            return dist
        for i in range(4):
            srcI = currI + row[i]
            srcJ = currJ + col[i]
            if valid(srcI, srcJ, n, m) and visited[srcI][srcJ] == False and a[srcI][srcJ] == 1:
                visited[srcI][srcJ] = True
                q.append((srcI, srcJ, dist + 1))
    return -1


for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    posI, posJ = map(int, input().split())
    a = [[0] * m for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(m):
            a[i][j] = l[k]
            k += 1
    print(shortestPath(0, 0, posI, posJ, n, m, a))
