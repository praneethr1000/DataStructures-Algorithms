# To increase recursion depth
import sys
sys.setrecursionlimit(100000)

def safe(i,j,n,m,A,visited):
    return i >= 0 and i < n and j >= 0 and j < m and A[i][j] == 1 and visited[i][j] == False

def dfs(visited,i,j,A,n,m):
    visited[i][j] = True
    # Eight positions
    row = [-1,-1,-1,0,0,1,1,1]
    col = [-1,0,1,-1,1,-1,0,1]
    for k in range(8):
        if safe(i+row[k],j+col[k],n,m,A,visited):
            dfs(visited,i+row[k],j+col[k],A,n,m)


def findIslands(A, N, M):
    count = 0
    visited = [[False for i in range(M)]for j in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and A[i][j] == 1:
                dfs(visited,i,j,A,N,M)
                count += 1
    return count