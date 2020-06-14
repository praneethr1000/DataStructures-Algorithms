def heapify(arr,n,i):
    l = (2*i)+1
    r = (2*i)+2
    largest = i
    if l < n  and arr[l] > arr[largest]:
        largest = l
    if r < n  and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
    print(arr)

l = [2,4,3,5,1]
heapsort(l)

