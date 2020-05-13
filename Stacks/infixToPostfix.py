def infixToPostfix(l):
    l1 = list(l)
    stack = []
    prec = {"^":3,"*":2,"/":2,"+":1,"-":1,"(":0}
    string = ""
    operands = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz")
    for x in l1:
        if x in operands :
            string += x
        elif x == '(':
            stack.append(x)
        elif x == ')':
            y = stack.pop()
            while y != '(':
                string += y
                y = stack.pop()
        else:
            if len(stack) > 0:
                y = stack[-1]
                while prec[x] <= prec[y]:
                    string += stack.pop()
                    if len(stack) != 0:
                        y = stack[-1]
                    else:
                        break
                stack.append(x)
            else:
                stack.append(x)
    while len(stack) != 0:
        string += stack.pop()
    return string

print(infixToPostfix("(A+B)+(C-D)"))




