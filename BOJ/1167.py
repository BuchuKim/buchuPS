from collections import deque
from sys import stdin;read=stdin.readline
N = int(read())
_graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    g = list(map(int,read().split()))[1:-1]
    print(g)
    for j in range(len(g)//2):
        _graph[i].append((g[2*j],g[2*j+1]))
def search(V):
    jirum = 0
    farnode = 0
    visited = [-1 for _ in range(N+1)]
    visited[V] = 0
    bfsQ = deque()
    bfsQ.append(V)
    while bfsQ:
        V = bfsQ.popleft()
        for i,j in _graph[V]:
            if (visited[i]==-1):
                visited[i] = visited[V] + j
                bfsQ.append(i)
                if (visited[i]>jirum):
                    jirum = visited[i]
                    farnode = i
    return jirum, farnode
_, node = search(1)
answer,node = search(node)
print(answer)