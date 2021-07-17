from collections import deque
import sys
N = int(sys.stdin.readline())

q = deque()
for _ in range(N):
    command = list(sys.stdin.readline().split())
    c = command[0]
    if (c=="push"):
        q.append(command[1])
    elif (c=="pop"):
        if (len(q)==0):
            print(-1)
        else:
            print(q.popleft())
    elif (c=="size"):
        print(len(q))
    elif (c=="empty"):
        if (len(q)==0):
            print(1)
        else:
            print(0)
    elif (c=="front"):
        if (len(q)==0):
            print(-1)
        else:
            ans = q.popleft()
            print(ans)
            q.appendleft(ans)
    elif (c=="back"):
        if (len(q)==0):
            print(-1)
        else:
            ans = q.pop()
            print(ans)
            q.append(ans)