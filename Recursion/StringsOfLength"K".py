def rangeToList(k):
    return [str(l) for l in range(k)]
def baseKStrings(n,k):
    if n == 0:
        return []
    if n == 1:
        return rangeToList(k)
    return [digit+bitstring for digit in baseKStrings(1,k) for bitstring in baseKStrings(n-1,k)]
print(baseKStrings(3,2))