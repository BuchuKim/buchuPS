import sys
from heapq import heappush,heappop
inf = sys.maxsize
read = sys.stdin.readline
N = int(read())
M = int(read())
graph = [[] for _ in range(N+1)]
dis = [inf] * (N+1)
for _ in range(M):
    a,b,t = map(int,read().split())
    graph[a].append([b,t])
s,e = map(int,read().split())
def search():
    dis[s] = 0
    heap = []
    heappush(heap,[0,s])
    while heap:
        cost,node = heappop(heap)
        if (dis[node]<cost):
            continue
        for des,dcost in graph[node]:
            if (dis[des]>cost+dcost):
                dis[des] = cost+dcost
                heappush(heap,[dis[des],des])
search()
print(dis[e])