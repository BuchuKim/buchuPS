import sys; read = sys.stdin.readline
from heapq import heappush,heappop
inf = sys.maxsize
n,m,r = map(int,read().split()) # 지역개수, 수색범위, 길의개수
graph = [[] for _ in range(n+1)]
items = [0] + list(map(int,read().split())) # 각 지역에 있는 아이템 갯수
for _ in range(r):
    a,b,l = map(int,read().split())
    # 양방향
    graph[a].append([b,l])
    graph[b].append([a,l])
def search(start):
    ans = 0
    heap = []
    dis = [inf] * (n+1)
    dis[start] = 0
    heappush(heap,[0,start])
    while heap:
        cost,node = heappop(heap)
        for des,dcost in graph[node]:
            if (dis[des]>cost+dcost):
                dis[des] = cost+dcost
                heappush(heap,[dis[des],des])
    for i in range(1,n+1):
        if (dis[i]<=m):
            ans += items[i]
    return ans
answer = 0
for i in range(1,n+1):
    answer = max(answer,search(i))
print(answer)