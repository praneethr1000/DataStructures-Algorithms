def maxInMinHeap(arr):
    maxi = -1
    for i in range((len(arr)+1)//2,len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi
