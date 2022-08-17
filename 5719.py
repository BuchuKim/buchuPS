import sys;input=sys.stdin.readline
from heapq import heappush,heappop
from collections import deque
INF = 1e9
def search():
    global dis, road, n, s,d
    heap = [(0,s)]
    while heap:
        cost,mid = heappop(heap)
        if dis[mid]<cost:
            continue
        for des in road[mid]:
            descost = road[mid][des]
            if (dis[des]>cost+descost):
                dis[des] = cost+descost
                heappush(heap,[dis[des],des])

def pathSearch():
    global road,r_road,s,d,remove
    Q = deque([d])
    while Q:
        node = Q.popleft()
        if node==s:
            continue
        for pre_node in r_road[node]:
            if dis[pre_node]+road[pre_node][node]==dis[node]:
                if (pre_node,node) not in remove:
                    remove.add((pre_node,node))
                    Q.append(pre_node)

while True:
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    s,d = map(int,input().split())
    road,r_road = [dict() for _ in range(n)], [[] for _ in range(n)]
    for _ in range(m):
        u,v,p = map(int,input().split())
        road[u][v] = p
        r_road[v].append(u)
    dis = [INF] * n
    dis[s] = 0
    search()
    remove = []
    pathSearch()
    for start,end in remove:
        del road[start][end]
    dis = [INF] * n
    dis[s] = 0
    search()
    if dis[d]<INF:
        print(dis[d])
    else:
        print(-1)