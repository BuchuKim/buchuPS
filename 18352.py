import sys;input=sys.stdin.readline
import heapq

n,m,k,x = map(int,input().split())
ansdis = [1000000 for _ in range(n+1)]
ansdis[x] = 0
path = dict()
for i in range(n+1):
    path[i] = []

for _ in range(m):
    a,b = map(int,input().split())
    path[a].append(b)

heap = [(0,x)]
while heap:
    d, cur = heapq.heappop(heap)
    for node in path[cur]:
        if (ansdis[node] > d+1):
            ansdis[node] = d+1
            heapq.heappush(heap,(ansdis[node],node))

ans = []
for i in range(1,n+1):
    if ansdis[i]==k:
        ans.append(i)
        print(i)

if (len(ans)==0):
    print(-1)