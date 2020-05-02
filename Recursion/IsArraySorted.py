def is_sorted(l):
    if len(l) == 1:
        return True
    return l[0] <= l[1] and is_sorted(l[1:])

arr = [1, 2, 3, 4]
print(is_sorted(arr))
