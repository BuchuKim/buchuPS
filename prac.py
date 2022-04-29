import sys;read=sys.stdin.readline
from heapq import heappop,heappush
inf = sys.maxsize
n,m,x = map(int,read().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int,read().split())
    graph[s].append([e,t])
def search(v):
    heap = [[0,v]]
    dis = [inf for _ in range(n+1)]
    dis[v] = 0
    while heap:
        cost, node = heappop(heap)
        if (cost>dis[node]):
            continue
        for des,descost in graph[node]:
            if (dis[des]>descost+cost):
                dis[des] = descost+cost
                heappush(heap,[dis[des],des])
    if (v==x):
        return dis
    else:
        return dis[x]
dis = search(x)
for i in range(1,n+1):
    if (i==x):
        continue
    dis[i] += search(i)
print(max(dis[1:]))