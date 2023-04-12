import sys;read=sys.stdin.readline
from collections import deque
N = int(read())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,read().split())
    graph[a].append(b)
    graph[b].append(a)
def search():
    visited = [0 for _ in range(N+1)]
    bfsQ = deque()
    bfsQ.append(1)
    visited[1] = 1
    while bfsQ:
        v = bfsQ.popleft()
        for i in graph[v]:
            if (visited[i]==0):
                visited[i] = v
                bfsQ.append(i)
    return visited
ans = search()
for i in range(2,N+1):
    print(ans[i])