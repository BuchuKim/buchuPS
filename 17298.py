import sys;input=sys.stdin.readline
from collections import deque
n = int(input())
li = list(map(int,input().split()))
ans = [0 for _ in range(n)]
ans[-1] = -1
dec = deque()
for i in range(1,n):
    dec.append(i-1)
    if li[i]>li[dec[-1]]:
        while dec and li[dec[-1]]<li[i]:
            ans[dec.pop()] = li[i]
for i in dec:
    ans[i] = -1
print(*ans)