def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        small = i
        for j in range(i+1,n):
            if arr[small] > arr[j]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]

arr = [64, 34, 25, 12, 22, 11, 90]
selectionSort(arr)
print(arr)