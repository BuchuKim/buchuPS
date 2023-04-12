import sys;read=sys.stdin.readline
from heapq import heappop,heappush,heapify
for _ in range(int(read())):
    n,k = map(int,read().split())
    time = [0] + list(map(int,read().split()))
    parent = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        a,b = map(int,read().split())
        parent[b] += 1
        heappush(graph[a],[time[b],b])
    w = int(read())
    Q = []
    for i in range(1,n+1):
        if (parent[i]==0):
            Q.append([time[i],i])
    heapify(Q)
    finished = False
    while Q:
        _,v = heappop(Q)
        while graph[v]:
            _,i = heappop(graph[v])
            parent[i] -= 1
            if (parent[i]==0):
                time[i] += time[v]
                heappush(Q,[time[i],i])
                if (i==w):
                    finished = True
                    break
        if finished:
            break
    print(time[w])