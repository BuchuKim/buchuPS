import sys;read=sys.stdin.readline
from collections import deque
n,k = map(int,read().split())
arr = deque(read().rstrip())
stack = deque()
del_num = 0
stack.append(arr.popleft())
while del_num<k:
    if len(arr)==0:
        while len(stack)!=n-k:
            stack.pop()
        break
    if len(stack)==0:
        stack.append(arr.popleft())
    if stack[-1]<arr[0]:
        stack.pop()
        del_num += 1
    else:
        stack.append(arr.popleft())
ans = "".join(stack) + "".join(arr)
print(ans)