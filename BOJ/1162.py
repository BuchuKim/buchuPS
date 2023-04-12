import sys;input=sys.stdin.readline
from heapq import heappop,heappush

n,m,k = map(int,input().split())
road = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    road[a].append([b,c])
    road[b].append([a,c])
# dis[n][k] : k번 포장했을 때 거리 최소
dis = [[sys.maxsize for _ in range(k+1)] for _ in range(n+1)]
dis[1][0] = 0
Q = [[0,0,1]]
while Q:
    d,_k,node = heappop(Q)
    if dis[node][_k] < d:
        continue
    for des,cost in road[node]:
        # 포장 X
        if dis[des][_k]>dis[node][_k]+cost:
            dis[des][_k] = dis[node][_k] + cost
            heappush(Q,[dis[des][_k],_k,des])
        # 포장 O
        if _k+1<=k:
            if dis[node][_k]<dis[des][_k+1]:
                dis[des][_k+1] = dis[node][_k]
                heappush(Q,[dis[des][_k+1],_k+1,des])
ans = sys.maxsize
for i in range(k+1):
    ans = min(ans,dis[-1][i])
print(ans)