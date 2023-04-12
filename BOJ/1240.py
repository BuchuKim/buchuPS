import sys;input=sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

for _ in range(M):
    a,b = map(int,input().split())
    visited = [False for _ in range(N+1)]
    bfsQ = deque([[a,0]])
    visited[a] = True
    while bfsQ:
        node,cost = bfsQ.popleft()
        if node==b:
            print(cost)
            break
        for nei,c in tree[node]:
            if not visited[nei]:
                visited[nei] = True
                bfsQ.append([nei,cost+c])