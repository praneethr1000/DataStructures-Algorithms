'''Works without brackets'''
def infixEvaluation(l):
    l1 = list(l)
    operandStack = []
    operatorStack = []
    result = 0
    numbers = list("0123456789")
    for x in l1:
        while len(operatorStack) != 0 and len(operandStack) >= 2:
            x = operatorStack.pop()
            second = int(operandStack.pop())
            first = int(operandStack.pop())
            if x == "+":
                result += first + second
            elif x == "-":
                result += first - second
            elif x == "*":
                result += first * second
            elif x == "//":
                result += first // second
            elif x == "^":
                result += first ^ second
            operandStack.append(result)
            result = 0
        if x in numbers:
            operandStack.append(int(x))
        else:
            if len(operandStack) >= 2:
                second = int(operandStack.pop())
                first = int(operandStack.pop())
                if x == "+":
                    result += first + second
                elif x == "-":
                    result += first - second
                elif x == "*":
                    result += first * second
                elif x == "//":
                    result += first // second
                elif x == "^":
                    result += first ^ second
                operandStack.append(result)
                result = 0
            else:
                operatorStack.append(x)

    return operandStack[0]

print(infixEvaluation("2*3+4"))
