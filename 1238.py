from sys import stdin; read=stdin.readline
from heapq import heappush,heappop
N,M,X = map(int,read().split())
graph = [[] for _ in range(N+1)]
dis = [100000000 for _ in range(N+1)]
graph_r = [[] for _ in range(N+1)]
dis_r = [100000000 for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int,read().split())
    graph[a].append([b,t])
    graph_r[b].append([a,t])

def search(start,g,dis):
    # d: distance, g: graph, start: start node
    heap = []
    heappush(heap,[0,start])
    dis[start] = 0
    while heap:
        # node: visit안된 가장 적은 cost가진 노드, cost: start~node
        cost, node = heappop(heap)
        if (dis[node]<cost):
            # node가 heap에 있는 동안 적게 업뎃되면 넘어가!
            continue
        for mid,midcost in g[node]:
            # mid: node와 연결된 노드, midcost: node~mid
            if (dis[mid]>cost+midcost):
                dis[mid] = cost+midcost
                # node는 visit. 
                heappush(heap,[dis[mid],mid])

search(X,graph,dis)
search(X,graph_r,dis_r)
answer = 0
for i in range(1,N+1):
    answer = max(answer,dis[i]+dis_r[i])
print(answer)