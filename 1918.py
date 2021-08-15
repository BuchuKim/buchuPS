from collections import deque
shik = input()
stack = deque()
answer = ""
for i in range(len(shik)):
    if shik[i]==")":
        # TODO :  pop until "("
        a = stack.popleft()
        n1 = ""
        n2 = ""
        op = ""
        while (a=="("):
            if (a in "+-/*"):
                op = a
            else:
                n1 = a
    else:
        stack.append(shik[i])
        i += 1