import sys;input=sys.stdin.readline
from collections import deque
n,k = map(int,input().split())
li = deque([i for i in range(1,n+1)])
ans = deque()
while li:
    for _ in range(k-1):
        li.append(li.popleft())
    ans.append(li.popleft())
print("<",end='')
for i in range(n-1):
    print(ans[i],end=", ")
print(ans[-1],end='')
print(">")