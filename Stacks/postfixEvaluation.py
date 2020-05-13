def postfixEvaluation(l):
    l1 = list(l)
    stack = []
    operands = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz")
    result = 0
    for x in l1:
        if x in operands:
            stack.append(x)
        else:
            second = int(stack.pop())
            first = int(stack.pop())
            if x == "+":
                result += first + second
            elif x == "-":
                result += first - second
            elif x == "*":
                result += first * second
            elif x == "/":
                result += first // second
            elif x == "^":
                result += first ^ second
            stack.append(result)
            result = 0
    return stack[0]

print(postfixEvaluation("123*+5-"))