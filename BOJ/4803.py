import sys;input=sys.stdin.readline
from collections import deque
def search(v):
    global visited
    isTree = True
    bfsQ = deque([v])
    while bfsQ:
        v = bfsQ.popleft()
        if visited[v]:
            isTree = False
        visited[v] = True
        for nei in graph[v]:
            if not visited[nei]:
                bfsQ.append(nei)
    return isTree

cnt = 1
while True:
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False for _ in range(n+1)]
    ans = 0
    for i in range(1,n+1):
        if not visited[i]:
            if search(i):
                ans += 1
    if ans==0:
        print("Case "+str(cnt)+": No trees.")
    elif ans==1:
        print("Case "+str(cnt)+": There is one tree.")
    else:
        print("Case "+str(cnt)+": A forest of "+str(ans)+" trees.")
    cnt += 1