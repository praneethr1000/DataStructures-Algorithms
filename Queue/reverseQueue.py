def reverse(l):
    print(l)
    stk = []
    for i in range(len(l)):
        stk.append(l.pop())
    for i in stk:
        l.append(i)
    print(l)
reverse([1,2,3,4])
