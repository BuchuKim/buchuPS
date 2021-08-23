import sys; read=sys.stdin.readline
from heapq import heappush,heappop
N = int(read()) # 마을개수
M = int(read()) # 버스개수
inf = sys.maxsize
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,t = map(int,read().split())
    graph[a].append([b,t])
start,end = map(int,read().split())
def search():
    heap = []
    mpath = [0 for _ in range(N+1)]
    dis = [inf] * (N+1)
    dis[start] = 0
    heappush(heap,[0,start])
    while heap:
        cost,node = heappop(heap)
        if (cost>dis[node]):
            continue
        for des,descost in graph[node]:
            if (dis[des]>cost+descost):
                dis[des] = cost+descost
                mpath[des] = node # 이전노드 값 저장
                heappush(heap,[dis[des],des])
    path = [end]
    while True:
        if (mpath[path[-1]]==0):
            break
        path.append(mpath[path[-1]])
    return dis[end],path
ans1,ans2 = search()
print(ans1)
print(len(ans2))
for i in range(1,len(ans2)+1):
    print(ans2[-i],end=' ')
print()