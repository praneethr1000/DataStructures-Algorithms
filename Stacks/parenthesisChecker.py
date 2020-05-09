def check(l1):
    l = list(l1)
    open = list("[{(")
    closed = list("]})")
    checker = []
    for x in l:
        if x in open:
            checker.append(x)
        elif x in closed:
            index = closed.index(x)
            if len(checker) == 0:
                return "not balanced"
            if open[index] == checker[-1]:
                checker.pop()
            else:
                return "not balanced"
    if len(checker) == 0:
        return "balanced"
    else:
        return "not balanced"

l1 = "((A+B)+[C-D]}"
print(check(l1))