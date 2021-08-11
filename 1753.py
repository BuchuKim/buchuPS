import sys
from heapq import heappush,heappop
read = sys.stdin.readline
V,E = map(int,read().split())
start = int(read())
inf = sys.maxsize
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,t = map(int,read().split())
    graph[a].append([b,t])
dis = [inf] * (V+1)
dis[start] = 0
def search():
    heap = []
    heappush(heap,[0,start])
    while heap:
        cost,node = heappop(heap)
        for des,dcost in graph[node]:
            if (dis[des]>dcost+cost):
                dis[des] = dcost+cost
                heappush(heap,[dis[des],des])
search()
for i in range(1,V+1):
    if (dis[i]<inf):
        print(dis[i])
    else:
        print("INF")