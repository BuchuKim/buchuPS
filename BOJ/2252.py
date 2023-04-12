import sys;read=sys.stdin.readline
from collections import deque
N,M = map(int,read().split())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
for _ in range(M):
    a,b = map(int,read().split())
    graph[a].append(b)
    parent[b] += 1
def search(V):
    answer = []
    Q = deque()
    for v in V:
        Q.append(v)
    while Q:
        v = Q.popleft()
        for i in graph[v]:
            parent[i] -= 1
            if (parent[i]==0):
                Q.append(i)
        answer.append(v)
    return answer
Vs = []
for i in range(1,N+1):
    if parent[i]==0:
        Vs.append(i)
ans = search(Vs)
for a in ans:
    print(a,end=' ')
print()