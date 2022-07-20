import sys;input=sys.stdin.readline
from heapq import heappop, heappush
n = int(input())
station = []
for _ in range(n):
    station.append(list(map(int,input().split())))
l,p = map(int,input().split())
station.sort()
ans = 0
heap = []
i = 0
while p<l:
    while i<n and station[i][0]<=p:
        heappush(heap,-station[i][1])
        i += 1
    if heap:
        p -= heappop(heap)
        ans += 1
    else:
        print(-1)
        exit()
print(ans)