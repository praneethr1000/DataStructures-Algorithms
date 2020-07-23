def findCounts(arr, n):
    i = 0
    while i < n:
        if arr[i] <= 0:
            i += 1
            continue
        elementIndex = arr[i] - 1

        if arr[elementIndex] > 0:
            arr[i] = arr[elementIndex]
            arr[elementIndex] = -1

        else:
            arr[elementIndex] -= 1
            arr[i] = 0
            i += 1

    print("Below are counts of all elements")
    for i in range(0, n):
        print("%d -> %d" % (i + 1, abs(arr[i])))
    print("")

arr = [2, 3, 3, 2, 5]
findCounts(arr, len(arr))