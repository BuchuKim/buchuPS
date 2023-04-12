import sys;read=sys.stdin.readline
from heapq import heappop,heapify
heap = []
for _ in range(int(read())):
    d,w = map(int,read().split())
    # 점수가 가장 큰 애가 나오게된다.
    heap.append([-w,d])
heapify(heap)
workFull = [False for _ in range(1001)]
score=0
while heap:
    w,d = heappop(heap)
    while workFull[d]:
        d -= 1
        if d<1:
            break
    if d>=1:
        workFull[d] = True
        score -= w
print(score)