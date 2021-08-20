import sys; read=sys.stdin.readline
from collections import deque
N,K = map(int,read().split())
bfsQ = deque()
bfsQ.append([N,0])
visited = [-1 for _ in range(100001)]
visited[N] = 0
short = 100000
ans = 0
while bfsQ:
    V,a = bfsQ.popleft()
    if (a>short):
        continue
    if (V==K):
        if (a<short):
            short = a
            ans = 1
        elif (a==short):
            ans += 1
    if (2*V<100001 and (visited[2*V]==-1 or visited[2*V]==a+1)):
        visited[2*V] = a+1
        bfsQ.append([2*V,a+1])
    if (V+1<=K and (visited[V+1]==-1 or visited[V+1]==a+1)):
        visited[V+1] = a+1
        bfsQ.append([V+1,a+1])
    if (V>=1 and (visited[V-1]==-1 or visited[V-1]==a+1)):
        visited[V-1] = a+1
        bfsQ.append([V-1,a+1])
print(short)
print(ans)