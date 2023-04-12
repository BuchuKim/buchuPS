import sys;input=sys.stdin.readline
from collections import deque
n = int(input())
ans = 0
stack = deque([0])
for _ in range(n):
    x,y = map(int,input().split())
    if y>stack[-1]:
        ans += 1
        stack.append(y)
    else:
        while y<stack[-1]:
            stack.pop()
        if (stack[-1]<y):
            ans += 1
            stack.append(y)
print(ans)