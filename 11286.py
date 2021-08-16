import heapq
import sys
read = sys.stdin.readline
N = int(read())
heap = []
for _ in range(N):
    c = int(read())
    if (c==0):
        if (heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        if (c>0):
            heapq.heappush(heap,[c,c])
        else:
            heapq.heappush(heap,[-c,c])