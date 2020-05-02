def appendInFront(x,k):
    return [x+digit for digit in k]

def bitStrings(n):
    if n == 0:
        return []
    if n == 1:
        return ["0", "1"]
    return appendInFront("0", bitStrings(n-1)) + appendInFront("1", bitStrings(n-1))

print(bitStrings(4))