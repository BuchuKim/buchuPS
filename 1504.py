from sys import stdin,maxsize; read=stdin.readline
from heapq import heappush, heappop
inf = maxsize
N,E = map(int,read().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,read().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
v1,v2 = map(int,read().split())
dis1 = [inf for _ in range(N+1)] #1
dis2 = [inf for _ in range(N+1)] #v1
dis3 = [inf for _ in range(N+1)] #v2
def search(start,dis):
    dis[start] = 0
    heap = []
    heappush(heap,[0,start])
    while heap:
        cost,node = heappop(heap)
        for des,midcost in graph[node]:
            if (dis[des]>cost+midcost):
                dis[des] = cost+midcost
                heappush(heap,[dis[des],des])
search(1,dis1)
search(v1,dis2)
search(v2,dis3)
answer = min(dis1[v1]+dis2[v2]+dis3[N],dis1[v2]+dis3[v1]+dis2[N])
if (answer>inf):
    print(-1)
else:
    print(answer)