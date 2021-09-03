from collections import deque
sik = input()
operator = deque()
operand = deque()
for i in range(len(sik)):
    s = sik[i]
    if s in '+-':
        if (operator and operator[-1] in "+-*/"):
            while operator and operator[-1] in "+-*/":
                o = operand.pop()
                operand.append(o+operator.pop())
            operator.append(s)
        else:
            operator.append(s)
    elif s in '*/':
        if (operator and operator[-1] in "*/"):
            o = operand.pop()
            operand.append(o+operator.pop())
            operator.append(s)
        else:
            operator.append(s)
    elif s=='(':
        operator.append(s)
    elif s==')':
        while operator:
            o = operator.pop()
            if o=='(':
                break
            a = operand.pop()
            operand.append(a+o)
    else:
        operand.append(s)
ans = ''
while (operand or operator):
    if operator:
        ans = ans + operator.pop()
    if operand:
        ans = operand.pop() + ans
print(ans)