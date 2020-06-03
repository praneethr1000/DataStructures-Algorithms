def height(P):
    maxDepth = -1
    currentDepth = -1
    for i in range(0,len(P)):
        j = i
        currentDepth = 0
        while P[j] != -1:
            currentDepth += 1
            j = P[j]
        maxDepth = max(maxDepth,currentDepth)
    return maxDepth

P = [-1,0,1,6,6,0,0,2,7]
print(height(P))