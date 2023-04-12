import sys;read=sys.stdin.readline
from collections import deque
N,M = map(int,read().split())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
for _ in range(M):
    li = list(map(int,read().split()))
    for i in range(1,len(li)-1):
        b,a = li[i],li[i+1]
        parent[a] += 1
        graph[b].append(a)
def search(V):
    Q = deque()
    ans = []
    for v in V:
        Q.append(v)
    while Q:
        v = Q.popleft()
        for i in graph[v]:
            parent[i] -= 1
            if (parent[i]==0):
                Q.append(i)
        ans.append(v)
    return ans
Vs = []
for i in range(1,N+1):
    if parent[i]==0:
        Vs.append(i)
answer = search(Vs)
if (len(answer)<N):
    print(0)
else:
    for a in answer:
        print(a)