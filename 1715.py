import sys;read=sys.stdin.readline
import heapq
n = int(read())
heap = []
for _ in range(n):
    heap.append(int(read()))

heapq.heapify(heap)
ans = 0
while True:
    if len(heap)==1:
        print(ans)
        exit()
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += a+b
    heapq.heappush(heap,a+b)