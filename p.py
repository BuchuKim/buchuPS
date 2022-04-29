import sys; read=sys.stdin.readline
from heapq import heappush, heappop
inf = sys.maxsize
n = int(read())
m = int(read())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,c = map(int,read().split())
    graph[s].append([e,c])
start,end = map(int,read().split())

dis = [inf for _ in range(n+1)]
path = [0 for _ in range(n+1)]
dis[start] = 0
heap = [[0,start]]
while heap:
    cost,node = heappop(heap)
    if (cost>dis[node]):
        continue
    for des,dcost in graph[node]:
        if (dis[des]>dcost+cost):
            dis[des] = dcost+cost
            path[des] = node
            heappush(heap,[dis[des],des])

ans = [end]
cur = end
while (cur!=start):
    cur = path[cur]
    ans.append(cur)
print(dis[end])
print(len(ans))
for i in range(1,len(ans)+1):
    print(ans[-i],end=' ')
print()