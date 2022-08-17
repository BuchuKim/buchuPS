import sys;input=sys.stdin.readline
from heapq import heappush, heappop
ans,lec = 0,[]
for _ in range(int(input())):
    p,d = map(int,input().split())
    lec.append([d,p])
lec.sort()
heap = []
for d,p in lec:
    heappush(heap,p)
    if len(heap)>d:
        heappop(heap)
print(sum(heap))